from modelscope.pipelines import pipeline  # type: ignore
from modelscope.utils.constant import Tasks  # type: ignore

inference_pipeline = pipeline(
    task=Tasks.auto_speech_recognition,
    model="iic/speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-pytorch",
    model_revision="v2.0.4",
)

rec_result = inference_pipeline("./docs/video/test.m4a")
print(rec_result)
