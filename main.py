from google import genai
from google.genai import types
import dis, argparse, marshal, struct, json, magic, os, platform

class PYC_PY:
    def __init__(self, DATA,API_KEY,MODEL): 
        self.DATA = DATA
        self.API_KEY = API_KEY
        self.MODEL = MODEL
        
    def print_version(self):
        DATA = self.DATA
        MAGIC_NUMBER = DATA.read(4)
        PYVER_DECIMAL = str(struct.unpack('<H', MAGIC_NUMBER[:2])[0])
        file = open("Versions_magicnum.json", 'r')
        JSON_VERSIONS = json.load(file)
        file.close()
        VERSIONS_RESULT = JSON_VERSIONS['Python_versions'][PYVER_DECIMAL]
        return VERSIONS_RESULT

    def disassemble(self):
        self.DATA.seek(16)
        LOAD_MARSHAL = marshal.load(self.DATA)
        create_newfile = open(ASSEMBLY_FILEPATH, 'w')
        dis.dis(LOAD_MARSHAL, file = create_newfile)
        create_newfile.close()

        
    def GEMINI(self):
        client = genai.Client(api_key=self.API_KEY)
        file_assembly = open(ASSEMBLY_FILEPATH,'rb')
        assembly = file_assembly.read()
        file_assembly.close()
        prompt = f"""
        Info: {PYTHON_VERSION}
        Decompile this python bytecode. Don't add any comments.
        Only return the decompiled code, no need explaination.
        """
        response = client.models.generate_content(
          model=self.MODEL,
          contents=[
              types.Part.from_bytes(
                data=assembly,
                mime_type='text/plain',
              ),
              prompt
          ]
        )
        return response.text
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog = 'PY_DecompilerXGemini',
        description = """This script helps disassemble python's bytecode (.pyc) 
                         and sends the assembly code to GEMINI to analyse it
                         in order to return a python code.
                         Must use the same Python version with the bytecode (.pyc) when
                         disassembling""",
        epilog = 'The results from GEMINI is not always correct. Use with caution'
    )

    parser.add_argument('filename',help = "Define the path to file.pyc needed to be decompiled")
    parser.add_argument('--api', required = True, help = "Define the GEMINI API Key")
    parser.add_argument('--model',default = "gemini-3-flash-preview", help = "Define Gemini model (Default: gemini-3-flash-preview). For more info https://ai.google.dev/gemini-api/docs/models")
    ARGS = parser.parse_args()
    FILE = open(ARGS.filename, 'rb')
    ASSEMBLY_FILEPATH = "Assembled/" + os.path.basename(ARGS.filename)[:-4] + ".assembly"
    functions = PYC_PY(FILE, ARGS.api, ARGS.model)
    
    PYTHON_VERSION = functions.print_version()
    breakpoint()
    if platform.python_version()[:-2] in PYTHON_VERSION:
        if "Assembled" not in os.listdir(): os.mkdir("Assembled")
        functions.disassemble()
        print(f"Found version: {PYTHON_VERSION}")
        print("Waiting for Gemini response...")
        print(functions.GEMINI())
    else:
        print("[X] Can't detect Python version")
    FILE.close()
