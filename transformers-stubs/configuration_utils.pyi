import typing as T

class PretrainedConfig:

    _PreTrainedConfig = T.TypeVar("_PreTrainedConfig", bound="PretrainedConfig")
    model_type: str = ...
    output_hidden_states: bool = False
    output_attentions: bool = False
    use_cache: bool = True
    torchscript: bool = False
    use_bfloat16: bool = False
    # pruned_heads:
    is_encoder_decoder: bool = False
    is_decoder: bool = False
    max_length: int = 20
    min_length: int = 0
    do_sample: bool = ...
    early_stopping: bool = ...
    num_beams: int = ...
    temperature: float = ...
    top_k: int = ...
    top_p: float = ...
    repetition_penalty: float = ...
    length_penalty: float = ...
    no_repeat_ngram_size: int = ...
    # bad_words_ids:  = ...
    num_return_sequences: int = ...
    # architectures: Any = ...
    # finetuning_task: Any = ...
    id2label: T.Dict[int, str] = ...
    label2id: T.Dict[str, int] = ...
    # prefix: Any = ...
    # bos_token_id: T.Optional[int] = ...
    # pad_token_id: T.Optional[int] = ...
    # eos_token_id: T.Optional[int] = ...
    # decoder_start_token_id: T.Optional[int] = ...
    # task_specific_params: Any = ...
    # xla_device: Any = ...
    def __init__(self, output_hidden_states: bool) -> None: ...
    @property
    def num_labels(self) -> int: ...
    @num_labels.setter
    def num_labels(self, num_labels: int) -> None: ...
    def save_pretrained(self, save_directory: str) -> None: ...
    @T.overload
    @classmethod
    def from_pretrained(
        cls: T.Type[_PreTrainedConfig],
        return_unused_kwargs: T.Literal[False],
        cache_dir: T.Optional[str] = None,
        force_download: bool = False,
        resume_download: bool = False,
        proxies: T.Optional[T.Dict[str, str]] = None,
        **kwargs: T.Any,
    ) -> "_PreTrainedConfig": ...
    @T.overload
    @classmethod
    def from_pretrained(
        cls: T.Type[_PreTrainedConfig],
        pretrained_model_name_or_path: str,
        return_unused_kwargs: T.Literal[True] = True,
        cache_dir: T.Optional[str] = None,
        force_download: bool = False,
        resume_download: bool = False,
        proxies: T.Optional[T.Dict[str, str]] = None,
        output_hidden_states: bool = ...,
        **kwargs: T.Any,
    ) -> T.Tuple["_PreTrainedConfig", T.Dict[str, T.Any]]: ...
    @classmethod
    def get_config_dict(
        cls, pretrained_model_name_or_path: str, **kwargs: T.Any
    ) -> T.Tuple[T.Dict[str, T.Any], T.Dict[str, T.Any]]: ...
    @classmethod
    def from_dict(
        cls: T.Type["_PreTrainedConfig"],
        config_dict: T.Dict[str, T.Any],
        **kwargs: T.Any,
    ) -> "_PreTrainedConfig": ...
    @classmethod
    def from_json_file(cls, json_file: str) -> "_PreTrainedConfig": ...
    def to_diff_dict(self) -> T.Dict[str, T.Any]: ...
    def to_dict(self) -> T.Dict[str, T.Any]: ...
    def to_json_string(self, use_diff:bool=True) -> str: ...
    def to_json_file(self, json_file_path: str, use_diff: bool = True) -> None: ...
    def update(self, config_dict: T.Dict[str, T.Any]) -> None: ...
