# D3D12Umddi.h header


This header is used by Display. For more information, see
- [Display](../_display/index.md)

D3D12Umddi.h contain these programming interfaces:


## Callback functions

| Title   | Description   |
| ---- |:---- |
| [PFND3D12DDI_ALLOCATE_CB_0022 callback](nc-d3d12umddi-pfnd3d12ddi-allocate-cb-0022.md) | The pfnAllocateCb callback function controls heap allocation by using a D3D12DDICB_ALLOCATE_0022 value. |
| [PFND3D12DDI_BEGIN_END_QUERY_0003 callback](nc-d3d12umddi-pfnd3d12ddi-begin-end-query-0003.md) | The pfnBeginQuery callback function defines the beginning of the portion of a command list to which a query applies. |
| [PFND3D12DDI_CALCPRIVATECOMMANDQUEUESIZE_0023 callback](nc-d3d12umddi-pfnd3d12ddi-calcprivatecommandqueuesize-0023.md) | The pfnCalcPrivateCommandQueueSize callback function is used to calculate the size of a private command queue. |
| [PFND3D12DDI_CALCPRIVATECRYPTOSESSIONPOLICYSIZE_0030 callback](nc-d3d12umddi-pfnd3d12ddi-calcprivatecryptosessionpolicysize-0030.md) | Used to calculate a session policy size. |
| [PFND3D12DDI_CALCPRIVATECRYPTOSESSIONSIZE_0030 callback](nc-d3d12umddi-pfnd3d12ddi-calcprivatecryptosessionsize-0030.md) | Used to calculate a private session size. |
| [PFND3D12DDI_CALCPRIVATEOPENEDCRYPTOSESSIONPOLICYSIZE_0030 callback](nc-d3d12umddi-pfnd3d12ddi-calcprivateopenedcryptosessionpolicysize-0030.md) | Used to calculate the size of an opened session policy. |
| [PFND3D12DDI_CALCPRIVATEOPENEDCRYPTOSESSIONSIZE_0030 callback](nc-d3d12umddi-pfnd3d12ddi-calcprivateopenedcryptosessionsize-0030.md) | Used to calculate the size of an opened session. |
| [PFND3D12DDI_CALCPRIVATEOPENEDPROTECTEDRESOURCESESSIONSIZE_0030 callback](nc-d3d12umddi-pfnd3d12ddi-calcprivateopenedprotectedresourcesessionsize-0030.md) | Used to calculate the size of an opened protected resource session. |
| [PFND3D12DDI_CALCPRIVATEPROTECTEDRESOURCESESSIONSIZE_0030 callback](nc-d3d12umddi-pfnd3d12ddi-calcprivateprotectedresourcesessionsize-0030.md) | Used to calculate the size of a protected resource session. |
| [PFND3D12DDI_CALCPRIVATEVIDEODECODERHEAPSIZE_0032 callback](nc-d3d12umddi-pfnd3d12ddi-calcprivatevideodecoderheapsize-0032.md) | Used to calculate the size of a video decoder heap. |
| [PFND3D12DDI_CALCPRIVATEVIDEODECODERHEAPSIZE_0033 callback](nc-d3d12umddi-pfnd3d12ddi-calcprivatevideodecoderheapsize-0033.md) | Used to calculate the size of a video decoder heap. |
| [PFND3D12DDI_CALCPRIVATEVIDEODECODERSIZE_0032 callback](nc-d3d12umddi-pfnd3d12ddi-calcprivatevideodecodersize-0032.md) | Used to calculate the size of a video decoder. |
| [PFND3D12DDI_CALCPRIVATEVIDEOPROCESSORSIZE_0032 callback](nc-d3d12umddi-pfnd3d12ddi-calcprivatevideoprocessorsize-0032.md) | Used to calculate the size of a video processor. |
| [PFND3D12DDI_CALC_PRIVATE_PIPELINE_STATE_SIZE_0033 callback](nc-d3d12umddi-pfnd3d12ddi-calc-private-pipeline-state-size-0033.md) | Used to calculate the pipeline state size. |
| [PFND3D12DDI_CHECKEXISITINGRESOURCEALLOCATIONINFO_0022 callback](nc-d3d12umddi-pfnd3d12ddi-checkexisitingresourceallocationinfo-0022.md) | The pfnCheckExistingResourceAllocationInfo callback function supports checking existing resource allocation information. |
| [PFND3D12DDI_CHECKRESOURCEALLOCATIONINFO_0022 callback](nc-d3d12umddi-pfnd3d12ddi-checkresourceallocationinfo-0022.md) | The pfnCheckResourceAllocationInfo callback function supports checking resource allocation information. |
| [PFND3D12DDI_CREATECOMMANDQUEUE_0023 callback](nc-d3d12umddi-pfnd3d12ddi-createcommandqueue-0023.md) | The pfnCreateCommandQueue callback function is used to create command queue. |
| [PFND3D12DDI_CREATECRYPTOSESSIONPOLICY_0030 callback](nc-d3d12umddi-pfnd3d12ddi-createcryptosessionpolicy-0030.md) | Used to create a crypto session policy. |
| [PFND3D12DDI_CREATECRYPTOSESSION_0030 callback](nc-d3d12umddi-pfnd3d12ddi-createcryptosession-0030.md) | Used to create a crypto session. |
| [PFND3D12DDI_CREATEHEAPANDRESOURCE_0030 callback](nc-d3d12umddi-pfnd3d12ddi-createheapandresource-0030.md) | Used to simultaneously create a heap and resource. |
| [PFND3D12DDI_CREATEPROTECTEDRESOURCESESSION_0030 callback](nc-d3d12umddi-pfnd3d12ddi-createprotectedresourcesession-0030.md) | Used to create a protected resource session. |
| [PFND3D12DDI_CREATEVIDEODECODERHEAP_0032 callback](nc-d3d12umddi-pfnd3d12ddi-createvideodecoderheap-0032.md) | Used to create a video decoder heap. |
| [PFND3D12DDI_CREATEVIDEODECODERHEAP_0033 callback](nc-d3d12umddi-pfnd3d12ddi-createvideodecoderheap-0033.md) | Used to create a video decoder heap. |
| [PFND3D12DDI_CREATEVIDEODECODER_0032 callback](nc-d3d12umddi-pfnd3d12ddi-createvideodecoder-0032.md) | Used to create a video decoder. |
| [PFND3D12DDI_CREATEVIDEOPROCESSOR_0032 callback](nc-d3d12umddi-pfnd3d12ddi-createvideoprocessor-0032.md) | Used to create a video processor. |
| [PFND3D12DDI_CREATE_PIPELINE_STATE_0021 callback](nc-d3d12umddi-pfnd3d12ddi-create-pipeline-state-0021.md) | The pfnCreatePipelineState callback function creates a pipeline state. |
| [PFND3D12DDI_CREATE_PIPELINE_STATE_0033 callback](nc-d3d12umddi-pfnd3d12ddi-create-pipeline-state-0033.md) | Used to create a pipeline state. |
| [PFND3D12DDI_CREATE_PROTECTED_SESSION_CB_0030 callback](nc-d3d12umddi-pfnd3d12ddi-create-protected-session-cb-0030.md) | Used to create a protected session state. |
| [PFND3D12DDI_DEALLOCATE_CB_0022 callback](nc-d3d12umddi-pfnd3d12ddi-deallocate-cb-0022.md) | The pfnDeallocateCb callback function controls heap deallocation by using a D3D12DDICB_DEALLOCATE_0022 structure. |
| [PFND3D12DDI_DESTROYCRYPTOSESSIONPOLICY_0030 callback](nc-d3d12umddi-pfnd3d12ddi-destroycryptosessionpolicy-0030.md) | Used to destroy a crypto session. |
| [PFND3D12DDI_DESTROYCRYPTOSESSION_0030 callback](nc-d3d12umddi-pfnd3d12ddi-destroycryptosession-0030.md) | Used to destroy a crypto session. |
| [PFND3D12DDI_DESTROYPROTECTEDRESOURCESESSION_0030 callback](nc-d3d12umddi-pfnd3d12ddi-destroyprotectedresourcesession-0030.md) | Used to destroy a protected resource session. |
| [PFND3D12DDI_DESTROYVIDEODECODERHEAP_0032 callback](nc-d3d12umddi-pfnd3d12ddi-destroyvideodecoderheap-0032.md) | Used to destroy a video decoder heap. |
| [PFND3D12DDI_GETKEYBASEDATA_0030 callback](nc-d3d12umddi-pfnd3d12ddi-getkeybasedata-0030.md) | Used to get key base data. |
| [PFND3D12DDI_OPENCRYPTOSESSIONPOLICY_0030 callback](nc-d3d12umddi-pfnd3d12ddi-opencryptosessionpolicy-0030.md) | Used to open a crypto session policy. |
| [PFND3D12DDI_OPENCRYPTOSESSION_0030 callback](nc-d3d12umddi-pfnd3d12ddi-opencryptosession-0030.md) | Used to open a crypto session. |
| [PFND3D12DDI_OPENPROTECTEDRESOURCESESSION_0030 callback](nc-d3d12umddi-pfnd3d12ddi-openprotectedresourcesession-0030.md) | Used to open a protected resource session. |
| [PFND3D12DDI_RESOLVE_QUERY_DATA callback](nc-d3d12umddi-pfnd3d12ddi-resolve-query-data.md) | The pfnResolveQueryData callback function transforms a previously stored query into an API defined format. |
| [PFND3D12DDI_RESOURCEBARRIER_0022 callback](nc-d3d12umddi-pfnd3d12ddi-resourcebarrier-0022.md) | The pfnResourceBarrier callback function supports resource barriers. |
| [PFND3D12DDI_SETPROTECTEDRESOURCESESSION_0030 callback](nc-d3d12umddi-pfnd3d12ddi-setprotectedresourcesession-0030.md) | Used to set a protected resource session. |
| [PFND3D12DDI_SETVIEWINSTANCEMASK_0033 callback](nc-d3d12umddi-pfnd3d12ddi-setviewinstancemask-0033.md) | Used to set a view instance mask. |
| [PFND3D12DDI_SET_EXTENDED_FEATURE_CALLBACKS_0021 callback](nc-d3d12umddi-pfnd3d12ddi-set-extended-feature-callbacks-0021.md) | The pfnSetExtendedFeatureCallbacks callback function sets extended feature callbacks. |
| [PFND3D12DDI_SET_PREDICATION callback](nc-d3d12umddi-pfnd3d12ddi-set-predication.md) | The pfnSetPredication callback function denotes that subsequent video operations and resource manipulation commands are not actually performed if the resulting predicate data of the predicate is equal to the operation specified. |
| [PFND3D12DDI_SHADERCACHEGETVALUE_CB_0021 callback](nc-d3d12umddi-pfnd3d12ddi-shadercachegetvalue-cb-0021.md) | The pfnShaderCacheGetValueCb callback function gets a shader cache value. |
| [PFND3D12DDI_SHADERCACHESTOREVALUE_CB_0021 callback](nc-d3d12umddi-pfnd3d12ddi-shadercachestorevalue-cb-0021.md) | The pfnShaderCacheStoreValueCb callback function stores a shader cache value. |
| [PFND3D12DDI_TRANSFORMENCRYPTEDDATA_0030 callback](nc-d3d12umddi-pfnd3d12ddi-transformencrypteddata-0030.md) | Used to transform encrypted data. |
| [PFND3D12DDI_VIDEO_DECODE_FRAME_0030 callback](nc-d3d12umddi-pfnd3d12ddi-video-decode-frame-0030.md) | Used to decode a video frame. |
| [PFND3D12DDI_VIDEO_DECODE_FRAME_0032 callback](nc-d3d12umddi-pfnd3d12ddi-video-decode-frame-0032.md) | Used to decode a video frame. |
| [PFND3D12DDI_VIDEO_GETCAPS callback](nc-d3d12umddi-pfnd3d12ddi-video-getcaps.md) | The pfnGetCaps callback function defines an entry point for video specific caps. |
| [PFND3D12DDI_VIDEO_PROCESS_FRAME_0032 callback](nc-d3d12umddi-pfnd3d12ddi-video-process-frame-0032.md) | Used to process a video frame. |
| [PFND3D12DDI_WRITEBUFFERIMMEDIATE_0032 callback](nc-d3d12umddi-pfnd3d12ddi-writebufferimmediate-0032.md) | Used to create a write buffer. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [D3D12DDIARG_CREATECOMMANDQUEUE_0023 structure](ns-d3d12umddi-d3d12ddiarg-createcommandqueue-0023.md) | Contains arguments used to create a command queue. |
| [D3D12DDIARG_CREATEDEVICE_0003 structure](ns-d3d12umddi-d3d12ddiarg-createdevice-0003.md) | The D3D10DDIARG_CREATEDEVICE_0003 structure describes the display device to create. |
| [D3D12DDIARG_CREATE_CRYPTO_SESSION_0030 structure](ns-d3d12umddi-d3d12ddiarg-create-crypto-session-0030.md) | Creates a crypto session. |
| [D3D12DDIARG_CREATE_CRYPTO_SESSION_POLICY_0030 structure](ns-d3d12umddi-d3d12ddiarg-create-crypto-session-policy-0030.md) | Creates a crypto session policy. |
| [D3D12DDIARG_CREATE_PIPELINE_STATE_0033 structure](ns-d3d12umddi-d3d12ddiarg-create-pipeline-state-0033.md) | Creates a pipeline state. |
| [D3D12DDIARG_CREATE_PROTECTED_RESOURCE_SESSION_0030 structure](ns-d3d12umddi-d3d12ddiarg-create-protected-resource-session-0030.md) | Creates a protected resource session. |
| [D3D12DDIARG_CREATE_VIDEO_DECODER_0032 structure](ns-d3d12umddi-d3d12ddiarg-create-video-decoder-0032.md) | Creates a video decoder. |
| [D3D12DDIARG_CREATE_VIDEO_DECODER_HEAP_0032 structure](ns-d3d12umddi-d3d12ddiarg-create-video-decoder-heap-0032.md) | Creates a video decoder heap. |
| [D3D12DDIARG_CREATE_VIDEO_DECODER_HEAP_0033 structure](ns-d3d12umddi-d3d12ddiarg-create-video-decoder-heap-0033.md) | Create a video decoder heap. |
| [D3D12DDIARG_CREATE_VIDEO_PROCESSOR_0032 structure](ns-d3d12umddi-d3d12ddiarg-create-video-processor-0032.md) | Creates a video processor. |
| [D3D12DDIARG_OPENADAPTER structure](ns-d3d12umddi-d3d12ddiarg-openadapter.md) | The D3D12DDIARG_OPENADAPTER structure describes the graphics adapter object. |
| [D3D12DDIARG_OPEN_CRYPTO_SESSION_0030 structure](ns-d3d12umddi-d3d12ddiarg-open-crypto-session-0030.md) | Opens a crypto session. |
| [D3D12DDIARG_OPEN_CRYPTO_SESSION_POLICY_0030 structure](ns-d3d12umddi-d3d12ddiarg-open-crypto-session-policy-0030.md) | Opens a crypto session policy. |
| [D3D12DDIARG_OPEN_PROTECTED_RESOURCE_SESSION_0030 structure](ns-d3d12umddi-d3d12ddiarg-open-protected-resource-session-0030.md) | Opens a protected resource session. |
| [D3D12DDIARG_RESOURCE_BARRIER_0022 structure](ns-d3d12umddi-d3d12ddiarg-resource-barrier-0022.md) | Describes a resource barrier. |
| [D3D12DDIARG_VIDEO_PROCESS_INPUT_STREAM_ARGUMENTS_0032 structure](ns-d3d12umddi-d3d12ddiarg-video-process-input-stream-arguments-0032.md) | The video process input stream arguments. |
| [D3D12DDIARG_VIDEO_PROCESS_OUTPUT_STREAM_ARGUMENTS_0032 structure](ns-d3d12umddi-d3d12ddiarg-video-process-output-stream-arguments-0032.md) | The video process output stream arguments. |
| [D3D12DDICAPS_UMD_BASED_COMMAND_QUEUE_PRIORITY_DATA_0023 structure](ns-d3d12umddi-d3d12ddicaps-umd-based-command-queue-priority-data-0023.md) | Contains priority data for a user-mode driver (UMD)-based command queue. |
| [D3D12DDICB_ALLOCATE_0022 structure](ns-d3d12umddi-d3d12ddicb-allocate-0022.md) | Specifies information for use in an allocation callback function. |
| [D3D12DDICB_DEALLOCATE_0022 structure](ns-d3d12umddi-d3d12ddicb-deallocate-0022.md) | Specifies values for use with a deallocation callback function. |
| [D3D12DDI_ALLOCATION_INFO_0022 structure](ns-d3d12umddi-d3d12ddi-allocation-info-0022.md) | Specifies allocation information. |
| [D3D12DDI_COMMAND_LIST_FUNCS_3D_0030 structure](ns-d3d12umddi-d3d12ddi-command-list-funcs-3d-0030.md) | The command list functions for 3D. |
| [D3D12DDI_COMMAND_LIST_FUNCS_3D_0032 structure](ns-d3d12umddi-d3d12ddi-command-list-funcs-3d-0032.md) | The command list functions for 3D. |
| [D3D12DDI_COMMAND_LIST_FUNCS_3D_0033 structure](ns-d3d12umddi-d3d12ddi-command-list-funcs-3d-0033.md) | The command list functions for 3D. |
| [D3D12DDI_COMMAND_LIST_FUNCS_VIDEO_DECODE_0030 structure](ns-d3d12umddi-d3d12ddi-command-list-funcs-video-decode-0030.md) | Command list functions for video decode. |
| [D3D12DDI_COMMAND_LIST_FUNCS_VIDEO_DECODE_0032 structure](ns-d3d12umddi-d3d12ddi-command-list-funcs-video-decode-0032.md) | Command list functions for video decode. |
| [D3D12DDI_COMMAND_LIST_FUNCS_VIDEO_PROCESS_0030 structure](ns-d3d12umddi-d3d12ddi-command-list-funcs-video-process-0030.md) | Command list functions for video process. |
| [D3D12DDI_COMMAND_LIST_FUNCS_VIDEO_PROCESS_0032 structure](ns-d3d12umddi-d3d12ddi-command-list-funcs-video-process-0032.md) | The command list functions for video processing. |
| [D3D12DDI_CONTENT_PROTECTION_CALLBACKS_0030 structure](ns-d3d12umddi-d3d12ddi-content-protection-callbacks-0030.md) | Content protection callbacks. |
| [D3D12DDI_CORELAYER_DEVICECALLBACKS_0022 structure](ns-d3d12umddi-d3d12ddi-corelayer-devicecallbacks-0022~r1.md) | This structure contains runtime callback functions that the user-mode display driver can use. |
| [D3D12DDI_CRYPTO_SESSION_TRANSFORM_DECRYPT_HEADER_INPUT_ARGUMENTS_0030 structure](ns-d3d12umddi-d3d12ddi-crypto-session-transform-decrypt-header-input-arguments-0030.md) | Crypto session transform decrypt header input arguments. |
| [D3D12DDI_CRYPTO_SESSION_TRANSFORM_DECRYPT_HEADER_OUTPUT_ARGUMENTS_0030 structure](ns-d3d12umddi-d3d12ddi-crypto-session-transform-decrypt-header-output-arguments-0030.md) | Crypto session transform decrypt header output arguments. |
| [D3D12DDI_CRYPTO_SESSION_TRANSFORM_DECRYPT_OUTPUT_ARGUMENTS_0030 structure](ns-d3d12umddi-d3d12ddi-crypto-session-transform-decrypt-output-arguments-0030.md) | Crypt session transform decrypt output arguments. |
| [D3D12DDI_CRYPTO_SESSION_TRANSFORM_INPUT_ARGUMENTS_0030 structure](ns-d3d12umddi-d3d12ddi-crypto-session-transform-input-arguments-0030.md) | Crypto session transform input arguments. |
| [D3D12DDI_CRYPTO_SESSION_TRANSFORM_OUTPUT_ARGUMENTS_0030 structure](ns-d3d12umddi-d3d12ddi-crypto-session-transform-output-arguments-0030.md) | Crypto session transform output arguments. |
| [D3D12DDI_CRYPTO_SESSION_TRANSFORM_TRANSCRYPT_OUTPUT_ARGUMENTS_0030 structure](ns-d3d12umddi-d3d12ddi-crypto-session-transform-transcrypt-output-arguments-0030.md) | Crypto session transform transcrypt output arguments. |
| [D3D12DDI_D3D12_OPTIONS_DATA_0031 structure](ns-d3d12umddi-d3d12ddi-d3d12-options-data-0031.md) | Display options data. |
| [D3D12DDI_D3D12_OPTIONS_DATA_0032 structure](ns-d3d12umddi-d3d12ddi-d3d12-options-data-0032.md) | Display options data. |
| [D3D12DDI_D3D12_OPTIONS_DATA_0033 structure](ns-d3d12umddi-d3d12ddi-d3d12-options-data-0033.md) | Display options data. |
| [D3D12DDI_DEVICE_FUNCS_CONTENT_PROTECTION_STREAMING_0030 structure](ns-d3d12umddi-d3d12ddi-device-funcs-content-protection-streaming-0030.md) | Device function for content protection streaming. |
| [D3D12DDI_DEVICE_FUNCS_CORE_0010 structure](ns-d3d12umddi-d3d12ddi-device-funcs-core-0010.md) | Contains core functions. |
| [D3D12DDI_DEVICE_FUNCS_CORE_0021 structure](ns-d3d12umddi-d3d12ddi-device-funcs-core-0021.md) | Specifies core device functions. |
| [D3D12DDI_DEVICE_FUNCS_CORE_0030 structure](ns-d3d12umddi-d3d12ddi-device-funcs-core-0030.md) | Core device functions. |
| [D3D12DDI_DEVICE_FUNCS_CORE_0033 structure](ns-d3d12umddi-d3d12ddi-device-funcs-core-0033.md) | Core device functions. |
| [D3D12DDI_DEVICE_FUNCS_CORE_VIDEO_0020 structure](ns-d3d12umddi-d3d12ddi-device-funcs-core-video-0020.md) | This structure contains device functions for core features in video. |
| [D3D12DDI_DEVICE_FUNCS_VIDEO_0030 structure](ns-d3d12umddi-d3d12ddi-device-funcs-video-0030.md) | Video device functions. |
| [D3D12DDI_DEVICE_FUNCS_VIDEO_0032 structure](ns-d3d12umddi-d3d12ddi-device-funcs-video-0032.md) | Video device functions. |
| [D3D12DDI_DEVICE_FUNCS_VIDEO_0033 structure](ns-d3d12umddi-d3d12ddi-device-funcs-video-0033.md) | The device functions of video. |
| [D3D12DDI_EXTENDED_FEATURES_FUNCS_0020 structure](ns-d3d12umddi-d3d12ddi-extended-features-funcs-0020.md) | This structure contains device functions for extended features in video. |
| [D3D12DDI_EXTENDED_FEATURES_FUNCS_0021 structure](ns-d3d12umddi-d3d12ddi-extended-features-funcs-0021.md) | Specifies callback functions for extended features. |
| [D3D12DDI_PROTECTED_RESOURCE_SESSION_SUPPORT_DATA_0030 structure](ns-d3d12umddi-d3d12ddi-protected-resource-session-support-data-0030.md) | Protected resource session support data. |
| [D3D12DDI_RANGE structure](ns-d3d12umddi-d3d12ddi-range.md) | Specifies a range. |
| [D3D12DDI_RESOURCE_ALLOCATION_INFO_0022 structure](ns-d3d12umddi-d3d12ddi-resource-allocation-info-0022.md) | Specifies information for resource allocation. |
| [D3D12DDI_RESOURCE_RANGED_BARRIER_0022 structure](ns-d3d12umddi-d3d12ddi-resource-ranged-barrier-0022.md) | Describes a resource ranged barrier. |
| [D3D12DDI_RESOURCE_TRANSITION_BARRIER_0003 structure](ns-d3d12umddi-d3d12ddi-resource-transition-barrier-0003.md) | Describes a transition barrier between subresources. |
| [D3D12DDI_RESOURCE_UAV_BARRIER structure](ns-d3d12umddi-d3d12ddi-resource-uav-barrier.md) | Contains an unordered access view (UAV) barrier. |
| [D3D12DDI_SHADERCACHE_CALLBACKS_0021 structure](ns-d3d12umddi-d3d12ddi-shadercache-callbacks-0021.md) | Specifies shader cache callback functions. |
| [D3D12DDI_SHADERCACHE_HASH structure](ns-d3d12umddi-d3d12ddi-shadercache-hash.md) | Includes a hash value. |
| [D3D12DDI_SWIZZLE_BIT_ENTRY structure](ns-d3d12umddi-d3d12ddi-swizzle-bit-entry.md) | Defines a swizzle bit entry. |
| [D3D12DDI_SWIZZLE_PATTERN_DESC_0022 structure](ns-d3d12umddi-d3d12ddi-swizzle-pattern-desc-0022.md) | Describes a swizzle pattern. |
| [D3D12DDI_TEXTURE_LAYOUT_CAPS_0001 structure](ns-d3d12umddi-d3d12ddi-texture-layout-caps-0001.md) | Specifies texture layout capabilities. |
| [D3D12DDI_TEXTURE_LAYOUT_CAPS_0026 structure](ns-d3d12umddi-d3d12ddi-texture-layout-caps-0026.md) | Specifies texture layout capabilities. |
| [D3D12DDI_VIDEO_CONTENT_PROTECTION_SYSTEM_COUNT_DATA_0030 structure](ns-d3d12umddi-d3d12ddi-video-content-protection-system-count-data-0030.md) | Video content protection system count data. |
| [D3D12DDI_VIDEO_CONTENT_PROTECTION_SYSTEM_SUPPORT_DATA_0030 structure](ns-d3d12umddi-d3d12ddi-video-content-protection-system-support-data-0030.md) | Video content protection system support data. |
| [D3D12DDI_VIDEO_CRYPTO_SESSION_SUPPORT_DATA_0030 structure](ns-d3d12umddi-d3d12ddi-video-crypto-session-support-data-0030.md) | Video crypto session support data. |
| [D3D12DDI_VIDEO_CRYPTO_SESSION_TRANSFORM_SUPPORT_DATA_0030 structure](ns-d3d12umddi-d3d12ddi-video-crypto-session-transform-support-data-0030.md) | Video crypto session transform support data. |
| [D3D12DDI_VIDEO_DECODER_HEAP_SIZE_DATA_0032 structure](ns-d3d12umddi-d3d12ddi-video-decoder-heap-size-data-0032.md) | Data structure for the D3D12DDICAPS_TYPE_VIDEO_0032_DECODER_HEAP_SIZE capability check. Retrieves the memory allocation size of a video decoder heap created with the given properties. |
| [D3D12DDI_VIDEO_DECODER_HEAP_SIZE_DATA_0033 structure](ns-d3d12umddi-d3d12ddi-video-decoder-heap-size-data-0033.md) | The video decoder heap size data. |
| [D3D12DDI_VIDEO_DECODE_BITSTREAM_ENCRYPTION_SCHEME_COUNT_DATA_0032 structure](ns-d3d12umddi-d3d12ddi-video-decode-bitstream-encryption-scheme-count-data-0032.md) | Video decode bitstream encryption scheme count data. |
| [D3D12DDI_VIDEO_DECODE_COMPRESSED_BITSTREAM_0032 structure](ns-d3d12umddi-d3d12ddi-video-decode-compressed-bitstream-0032.md) | Video decode compressed bitstream. |
| [D3D12DDI_VIDEO_DECODE_CONVERSION_SUPPORT_DATA_0032 structure](ns-d3d12umddi-d3d12ddi-video-decode-conversion-support-data-0032.md) | Video decode conversion support data. |
| [D3D12DDI_VIDEO_DECODE_DECRYPTION_ARGUMENTS_0030 structure](ns-d3d12umddi-d3d12ddi-video-decode-decryption-arguments-0030.md) | Video decode decryption arguments. |
| [D3D12DDI_VIDEO_DECODE_FORMAT_COUNT_DATA_0032 structure](ns-d3d12umddi-d3d12ddi-video-decode-format-count-data-0032.md) | Video decode format count data. |
| [D3D12DDI_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS_0030 structure](ns-d3d12umddi-d3d12ddi-video-decode-input-stream-arguments-0030.md) | Video decode input stream arguments. |
| [D3D12DDI_VIDEO_DECODE_INPUT_STREAM_ARGUMENTS_0032 structure](ns-d3d12umddi-d3d12ddi-video-decode-input-stream-arguments-0032.md) | Video decode input stream arguments. |
| [D3D12DDI_VIDEO_DECODE_PROFILE_COUNT_DATA_0032 structure](ns-d3d12umddi-d3d12ddi-video-decode-profile-count-data-0032.md) | Video decode profile count data. |
| [D3D12DDI_VIDEO_DECODE_REFERENCE_FRAMES_0032 structure](ns-d3d12umddi-d3d12ddi-video-decode-reference-frames-0032.md) | Video decode reference frames. |
| [D3D12DDI_VIDEO_PROCESSOR_INPUT_STREAM_DESC_0032 structure](ns-d3d12umddi-d3d12ddi-video-processor-input-stream-desc-0032.md) | Describes input stream properties for the video processor. |
| [D3D12DDI_VIDEO_PROCESSOR_SIZE_DATA_0032 structure](ns-d3d12umddi-d3d12ddi-video-processor-size-data-0032.md) | Data structure for the D3D12DDICAPS_TYPE_VIDEO_0032_PROCESSOR_SIZE capability check. Retrieves the memory allocation size of a video processor created with the given properties. |
| [D3D12DDI_VIDEO_PROCESS_INPUT_STREAM_RATE_INFO_0032 structure](ns-d3d12umddi-d3d12ddi-video-process-input-stream-rate-info-0032.md) | The video process input stream rate info. |
| [D3D12DDI_VIDEO_PROCESS_OUTPUT_STREAM_DESC_0032 structure](ns-d3d12umddi-d3d12ddi-video-process-output-stream-desc-0032.md) | Describes output stream properties for the video processor. |
| [D3D12DDI_VIDEO_PROCESS_SUPPORT_DATA_0032 structure](ns-d3d12umddi-d3d12ddi-video-process-support-data-0032.md) | Video process support data. |
| [D3D12DDI_VIDEO_PROCESS_TRANSFORM_0032 structure](ns-d3d12umddi-d3d12ddi-video-process-transform-0032.md) | Video process transform. |
| [D3D12DDI_VIDEO_SCALE_SUPPORT_0032 structure](ns-d3d12umddi-d3d12ddi-video-scale-support-0032.md) | Video scale support. |
| [D3D12DDI_VIDEO_SIZE_RANGE_0032 structure](ns-d3d12umddi-d3d12ddi-video-size-range-0032.md) | Video size range. |
| [D3D12DDI_VIEW_INSTANCE_LOCATION structure](ns-d3d12umddi-d3d12ddi-view-instance-location.md) | View instance location. |
| [D3D12DDI_VIEW_INSTANCING_DESC structure](ns-d3d12umddi-d3d12ddi-view-instancing-desc.md) | View instancing description. |
| [D3D12DDI_WRITEBUFFERIMMEDIATE_PARAMETER_0032 structure](ns-d3d12umddi-d3d12ddi-writebufferimmediate-parameter-0032.md) | Write buffer immediate parameter. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [D3D12DDICAPS_TYPE enumeration](ne-d3d12umddi-d3d12ddicaps-type.md) | Specifies a capability type. |
| [D3D12DDICAPS_TYPE_VIDEO_0020 enumeration](ne-d3d12umddi-d3d12ddicaps-type-video-0020.md) | Contains capability types for video. |
| [D3D12DDI_ALLOCATION_INFO_FLAGS_0022 enumeration](ne-d3d12umddi-d3d12ddi-allocation-info-flags-0022.md) | Contains allocation information flags. |
| [D3D12DDI_BITSTREAM_ENCRYPTION_TYPE_0030 enumeration](ne-d3d12umddi-d3d12ddi-bitstream-encryption-type-0030.md) | The bitstream encryption type. |
| [D3D12DDI_COMMAND_QUEUE_CREATION_FLAGS enumeration](ne-d3d12umddi-d3d12ddi-command-queue-creation-flags.md) | Defines command queue creation options. |
| [D3D12DDI_COMMAND_QUEUE_FLAGS enumeration](ne-d3d12umddi-d3d12ddi-command-queue-flags.md) | Contains values for the video command queue. |
| [D3D12DDI_CREATE_SHADER_FLAGS enumeration](ne-d3d12umddi-d3d12ddi-create-shader-flags.md) | Defines flags for shader creation. |
| [D3D12DDI_CRYPTO_SESSION_FLAGS_0030 enumeration](ne-d3d12umddi-d3d12ddi-crypto-session-flags-0030.md) | The crypto session flags. |
| [D3D12DDI_CRYPTO_SESSION_SUPPORT_FLAGS_0030 enumeration](ne-d3d12umddi-d3d12ddi-crypto-session-support-flags-0030.md) | The crypto session support flags. |
| [D3D12DDI_CRYPTO_SESSION_TRANSFORM_OPERATION_0030 enumeration](ne-d3d12umddi-d3d12ddi-crypto-session-transform-operation-0030.md) | The crypto session transform operations. |
| [D3D12DDI_CRYPTO_SESSION_TRANSFORM_SUPPORT_FLAGS_0030 enumeration](ne-d3d12umddi-d3d12ddi-crypto-session-transform-support-flags-0030.md) | The crypto session transform support flags. |
| [D3D12DDI_DEALLOCATE_FLAGS_0022 enumeration](ne-d3d12umddi-d3d12ddi-deallocate-flags-0022.md) | Defines flags for use in deallocation. |
| [D3D12DDI_FEATURE_0020 enumeration](ne-d3d12umddi-d3d12ddi-feature-0020.md) | Contains available features. |
| [D3D12DDI_HANDLETYPE enumeration](ne-d3d12umddi-d3d12ddi-handletype.md) | Contains driver handle types. |
| [D3D12DDI_HEAP_FLAGS enumeration](ne-d3d12umddi-d3d12ddi-heap-flags.md) | Contains Direct3D 12 heap flags. |
| [D3D12DDI_PREDICATION_OP enumeration](ne-d3d12umddi-d3d12ddi-predication-op.md) | Contains values for predication operation options. |
| [D3D12DDI_PROTECTED_RESOURCE_SESSION_SUPPORT_FLAGS_0030 enumeration](ne-d3d12umddi-d3d12ddi-protected-resource-session-support-flags-0030.md) | The protected resource session support flags. |
| [D3D12DDI_QUERY_HEAP_TYPE enumeration](ne-d3d12umddi-d3d12ddi-query-heap-type.md) | Type of a query heap, which is an array of query results. |
| [D3D12DDI_QUERY_TYPE enumeration](ne-d3d12umddi-d3d12ddi-query-type.md) | Type of a query. |
| [D3D12DDI_RESOURCE_BARRIER_FLAGS enumeration](ne-d3d12umddi-d3d12ddi-resource-barrier-flags.md) | Contains resource barrier flags. |
| [D3D12DDI_RESOURCE_BARRIER_TYPE enumeration](ne-d3d12umddi-d3d12ddi-resource-barrier-type.md) | Specifies the type of resource barrier. |
| [D3D12DDI_RESOURCE_FLAGS_0003 enumeration](ne-d3d12umddi-d3d12ddi-resource-flags-0003.md) | Specifies resource flag values. |
| [D3D12DDI_RESOURCE_STATES enumeration](ne-d3d12umddi-d3d12ddi-resource-states.md) | Contains resource states. |
| [D3D12DDI_SWIZZLE_PATTERN enumeration](ne-d3d12umddi-d3d12ddi-swizzle-pattern.md) | Specifies a swizzle pattern. |
| [D3D12DDI_SWIZZLE_PATTERN_FLAGS enumeration](ne-d3d12umddi-d3d12ddi-swizzle-pattern-flags.md) | Specifies swizzle pattern flags. |
| [D3D12DDI_TABLE_TYPE enumeration](ne-d3d12umddi-d3d12ddi-table-type.md) | Command list and queue types to allow drivers to point to different implementations for video. |
| [D3D12DDI_TEXTURE_LAYOUT enumeration](ne-d3d12umddi-d3d12ddi-texture-layout.md) | Specifies a texture layout. |
| [D3D12DDI_VIDEO_PROCESS_FILTER_0020 enumeration](ne-d3d12umddi-d3d12ddi-video-process-filter-0020.md) | Contains video process filters. |
| [D3D12DDI_VIDEO_USAGE enumeration](ne-d3d12umddi-d3d12ddi-video-usage.md) | A hint for the graphics driver to optimize for different scenarios. |
| [D3D12DDI_VIEW_INSTANCING_FLAGS enumeration](ne-d3d12umddi-d3d12ddi-view-instancing-flags.md) | Defines the view instancing flags. |
| [D3D12DDI_VIEW_INSTANCING_TIER enumeration](ne-d3d12umddi-d3d12ddi-view-instancing-tier.md) | Defines the view instancing tier. |
| [D3D12DDI_WRITEBUFFERIMMEDIATE_MODE_0032 enumeration](ne-d3d12umddi-d3d12ddi-writebufferimmediate-mode-0032.md) | The write buffer immediate mode. |
