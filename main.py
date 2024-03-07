from app.voice.base import VoiceBase
from app.api.base import APIBase
from app.prompts.base import PromptsBase
from app.chat.base import ChatBase
from app.brain.base import BrainBase
from app.cli.base import CLIBase
from app.db.base import DBBase
from app.embeddings.base import EmbeddingsBase
from app.ingest.base import IngestBase
from app.memory.base import MemoryBase
from app.messages.base import MessagesBase
from app.retriever.base import RetrieverBase


def main():
    print(VoiceBase.voice_in("test"))
    VoiceBase.voice_out("test")
    print(APIBase.call_api("test", {}))
    print(PromptsBase.load_prompt("test"))
    print(ChatBase.send_message("test"))
    print(ChatBase.receive_message())
    print(BrainBase.meth("hi"))
    print(CLIBase.meth("hi"))
    print(DBBase.meth("hi"))
    print(EmbeddingsBase.meth("hi"))
    print(IngestBase.meth("hi"))
    print(MemoryBase.meth("hi"))
    print(MessagesBase.meth("hi"))
    print(RetrieverBase.meth("hi"))


if __name__ == "__main__":
    main()
