# Netdma.h header


This header is used by Networking drivers for Windows Vista and later. For more information, see
- [Networking drivers for Windows Vista and later](../_netvista/index.md)

Netdma.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [NetDmaDeregisterProvider function](nf-netdma-netdmaderegisterprovider.md) | The NetDmaDeregisterProvider function deregisters a DMA provider. |
| [NetDmaGetVersion function](nf-netdma-netdmagetversion.md) | Note  The NetDMA interface is not supported in Windows 8 and later. The NetDmaGetVersion function returns the version of the NetDMA interface that the local computer supports. |
| [NetDmaInterruptDpc function](nf-netdma-netdmainterruptdpc.md) | The NetDmaInterruptDpc function notifies the NetDMA interface that a DMA transfer deferred procedure call (DPC) has completed on a DMA channel. |
| [NetDmaIsr function](nf-netdma-netdmaisr.md) | The NetDmaIsr function notifies the NetDMA interface that a DMA transfer interrupt has occurred on a DMA channel. |
| [NetDmaPnPEventNotify function](nf-netdma-netdmapnpeventnotify.md) | The NetDmaPnPEventNotify function indicates a power state change for a NetDMA provider device. |
| [NetDmaProviderStart function](nf-netdma-netdmaproviderstart.md) | The NetDmaProviderStart function notifies the NetDMA interface that all of the DMA channels that are associated with a DMA provider are initialized and ready for DMA transfers. |
| [NetDmaProviderStop function](nf-netdma-netdmaproviderstop.md) | The NetDmaProviderStop function notifies the NetDMA interface that all of the DMA channels that are associated with a DMA provider are no longer available for DMA transfers. |
| [NetDmaRegisterProvider function](nf-netdma-netdmaregisterprovider.md) | The NetDmaRegisterProvider function registers a DMA provider. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [DMA_ABORT_HANDLER callback](nc-netdma-dma-abort-handler.md) | The ProviderAbortDma function cancels any DMA transfers that are associated with a DMA channel. |
| [DMA_APPEND_HANDLER callback](nc-netdma-dma-append-handler.md) | The ProviderAppendDma function appends a linked list of DMA descriptors to the last descriptor on a DMA channel. |
| [DMA_CHANNELS_CPU_AFFINITY_HANDLER callback](nc-netdma-dma-channels-cpu-affinity-handler.md) | The ProviderSetDmaChannelCpuAffinity function sets the CPU affinities for the DMA channels that are associated with a DMA provider. |
| [DMA_CHANNEL_ALLOCATE_HANDLER callback](nc-netdma-dma-channel-allocate-handler.md) | The ProviderAllocateDmaChannel function allocates a DMA channel. |
| [DMA_CHANNEL_FREE_HANDLER callback](nc-netdma-dma-channel-free-handler.md) | The ProviderFreeDmaChannel function frees a DMA channel that the ProviderAllocateDmaChannel function previously allocated. |
| [DMA_RESET_HANDLER callback](nc-netdma-dma-reset-handler.md) | The ProviderResetChannel function resets a DMA channel to the initial state that existed after the DMA channel was allocated. |
| [DMA_RESUME_HANDLER callback](nc-netdma-dma-resume-handler.md) | The ProviderResumeDma function resumes the DMA transfers that are currently suspended on a DMA channel. |
| [DMA_START_HANDLER callback](nc-netdma-dma-start-handler.md) | The ProviderStartDma function starts a DMA transfer on the specified DMA channel. |
| [DMA_SUSPEND_HANDLER callback](nc-netdma-dma-suspend-handler.md) | The ProviderSuspendDma function suspends the DMA transfers that are currently in progress on a DMA channel. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [NET_DMA_CHANNEL_CPU_AFFINITY structure](ns-netdma--net-dma-channel-cpu-affinity.md) | The NET_DMA_CHANNEL_CPU_AFFINITY structure specifies the CPU affinity of a DMA channel. |
| [NET_DMA_CHANNEL_PARAMETERS structure](ns-netdma--net-dma-channel-parameters.md) | The NET_DMA_CHANNEL_PARAMETERS structure specifies the configuration parameters that a DMA provider driver should use to configure a DMA channel. |
| [NET_DMA_DESCRIPTOR structure](ns-netdma--net-dma-descriptor.md) | The NET_DMA_DESCRIPTOR structure specifies the DMA transfer information for each entry in a linked list of DMA descriptors. |
| [NET_DMA_PNP_NOTIFICATION structure](ns-netdma--net-dma-pnp-notification.md) | The NET_DMA_PNP_NOTIFICATION structure specifies a power management notification in the NetDMA interface. |
| [NET_DMA_PROVIDER_ATTRIBUTES structure](ns-netdma--net-dma-provider-attributes.md) | The NET_DMA_PROVIDER_ATTRIBUTES structure specifies the configuration attributes for a NetDMA provider. |
| [NET_DMA_PROVIDER_CHARACTERISTICS structure](ns-netdma--net-dma-provider-characteristics.md) | The NET_DMA_PROVIDER_CHARACTERISTICS structure specifies the characteristics for a NetDMA provider, including the entry points for the ProviderXxx functions. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [NET_DMA_PNP_NOTIFICATION_CODE enumeration](ne-netdma--net-dma-pnp-notification-code.md) | The NET_DMA_PNP_NOTIFICATION_CODE enumeration identifies the type of a NetDMA Plug and Play (PnP) event. |
