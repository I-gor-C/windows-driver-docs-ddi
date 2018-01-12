---
UID: NA:sercx
---

# Sercx.h header

## -description

This header is used by serports. For more information, see
- [serports](../_serports/index.md)

Sercx.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [SERCX2_CONFIG_INIT function](nf-sercx-sercx2_config_init.md) | The SERCX2_CONFIG_INIT function initializes a SERCX2_CONFIG structure. |
| [SERCX2_CUSTOM_RECEIVE_CONFIG_INIT function](nf-sercx-sercx2_custom_receive_config_init.md) | The SERCX2_CUSTOM_RECEIVE_CONFIG_INIT function initializes a SERCX2_CUSTOM_RECEIVE_CONFIG structure. |
| [SERCX2_CUSTOM_RECEIVE_TRANSACTION_CONFIG_INIT function](nf-sercx-sercx2_custom_receive_transaction_config_init.md) | The SERCX2_CUSTOM_RECEIVE_TRANSACTION_CONFIG_INIT function initializes a SERCX2_CUSTOM_RECEIVE_TRANSACTION_CONFIG structure. |
| [SERCX2_CUSTOM_TRANSMIT_CONFIG_INIT function](nf-sercx-sercx2_custom_transmit_config_init.md) | The SERCX2_CUSTOM_TRANSMIT_CONFIG_INIT function initializes a SERCX2_CUSTOM_TRANSMIT_CONFIG structure. |
| [SERCX2_CUSTOM_TRANSMIT_TRANSACTION_CONFIG_INIT function](nf-sercx-sercx2_custom_transmit_transaction_config_init.md) | The SERCX2_CUSTOM_TRANSMIT_TRANSACTION_CONFIG_INIT function initializes a SERCX2_CUSTOM_TRANSMIT_TRANSACTION_CONFIG structure. |
| [SERCX2_PIO_RECEIVE_CONFIG_INIT function](nf-sercx-sercx2_pio_receive_config_init.md) | The SERCX2_PIO_RECEIVE_CONFIG_INIT function initializes a SERCX2_PIO_RECEIVE_CONFIG structure. |
| [SERCX2_PIO_TRANSMIT_CONFIG_INIT function](nf-sercx-sercx2_pio_transmit_config_init.md) | The SERCX2_PIO_TRANSMIT_CONFIG_INIT function initializes a SERCX2_PIO_TRANSMIT_CONFIG structure. |
| [SERCX2_SYSTEM_DMA_RECEIVE_CONFIG_INIT function](nf-sercx-sercx2_system_dma_receive_config_init.md) | The SERCX2_SYSTEM_DMA_RECEIVE_CONFIG_INIT function initializes a SERCX2_SYSTEM_DMA_RECEIVE_CONFIG structure. |
| [SERCX2_SYSTEM_DMA_RECEIVE_CONFIG_INIT_NEW_DATA_NOTIFICATION function](nf-sercx-sercx2_system_dma_receive_config_init_new_data_notification.md) | The SERCX2_SYSTEM_DMA_RECEIVE_CONFIG_INIT_NEW_DATA_NOTIFICATION function initializes a SERCX2_SYSTEM_DMA_RECEIVE_CONFIG structure. |
| [SERCX2_SYSTEM_DMA_TRANSMIT_CONFIG_INIT function](nf-sercx-sercx2_system_dma_transmit_config_init.md) | The SERCX2_SYSTEM_DMA_TRANSMIT_CONFIG_INIT function initializes a SERCX2_SYSTEM_DMA_TRANSMIT_CONFIG structure. |
| [SERCX_ACTIVITY_INIT function](nf-sercx-sercx_activity_init.md) | The SERCX_ACTIVITY_INIT function initializes a SERCX_ACTIVITY structure. |
| [SERCX_BUFFER_DESCRIPTOR_INIT function](nf-sercx-sercx_buffer_descriptor_init.md) | The SERCX_BUFFER_DESCRIPTOR_INIT function initializes a SERCX_BUFFER_DESCRIPTOR structure. |
| [SERCX_CONFIG_INIT function](nf-sercx-sercx_config_init.md) | The SERCX_CONFIG_INIT function initializes a SERCX_CONFIG structure. |
| [SerCx2CompleteWait function](nf-sercx-sercx2completewait.md) | The SerCx2CompleteWait method notifies version 2 of the serial framework extension (SerCx2) that an event in the current wait mask has occurred. |
| [SerCx2CustomReceiveCreate function](nf-sercx-sercx2customreceivecreate.md) | The SerCx2CustomReceiveCreate method creates a custom-receive object, which version 2 of the serial framework extension (SerCx2) uses to read receive data from the serial controller by means of a custom data-transfer mechanism. |
| [SerCx2CustomReceiveTransactionCleanupComplete function](nf-sercx-sercx2customreceivetransactioncleanupcomplete.md) | The SerCx2CustomReceiveTransactionCleanupComplete method informs version 2 of the serial framework extension (SerCx2) that the serial controller driver has finished cleaning up the serial controller's hardware state after a custom-receive transaction. |
| [SerCx2CustomReceiveTransactionCreate function](nf-sercx-sercx2customreceivetransactioncreate.md) | The SerCx2CustomReceiveTransactionCreate method creates a custom-receive-transaction object, which version 2 of the serial framework extension (SerCx2) uses to perform custom-receive transactions. |
| [SerCx2CustomReceiveTransactionInitializeComplete function](nf-sercx-sercx2customreceivetransactioninitializecomplete.md) | The SerCx2CustomReceiveTransactionInitializeComplete method notifies version 2 of the serial framework extension (SerCx2) that the serial controller driver has finished initializing the serial controller and associated hardware in preparation for a new custom-receive transaction. |
| [SerCx2CustomReceiveTransactionNewDataNotification function](nf-sercx-sercx2customreceivetransactionnewdatanotification.md) | The SerCx2CustomReceiveTransactionNewDataNotification method notifies version 2 of the serial framework extension (SerCx2) that data is available to be read from the receive FIFO in the serial controller hardware. |
| [SerCx2CustomReceiveTransactionReportProgress function](nf-sercx-sercx2customreceivetransactionreportprogress.md) | The SerCx2CustomReceiveTransactionReportProgress method reports whether progress is being made toward completing the current custom-receive transaction. |
| [SerCx2CustomTransmitCreate function](nf-sercx-sercx2customtransmitcreate.md) | The SerCx2CustomTransmitCreate method creates a custom-transmit object, which version 2 of the serial framework extension (SerCx2) uses to write transmit data to the serial controller by means of a custom data-transfer mechanism. |
| [SerCx2CustomTransmitTransactionCleanupComplete function](nf-sercx-sercx2customtransmittransactioncleanupcomplete.md) | The SerCx2CustomTransmitTransactionCleanupComplete method notifies version 2 of the serial framework extension (SerCx2) that the serial controller driver has finished cleaning up the serial controller's hardware state after a custom-transmit transaction. |
| [SerCx2CustomTransmitTransactionCreate function](nf-sercx-sercx2customtransmittransactioncreate.md) | The SerCx2CustomTransmitTransactionCreate method creates a custom-transmit-transaction object, which version 2 of the serial framework extension (SerCx2) uses to perform custom-transmit transactions. |
| [SerCx2CustomTransmitTransactionInitializeComplete function](nf-sercx-sercx2customtransmittransactioninitializecomplete.md) | The SerCx2CustomTransmitTransactionInitializeComplete method informs version 2 of the serial framework extension (SerCx2) that the serial driver has finished initializing the serial controller and associated hardware in preparation for a new custom-transmit transaction. |
| [SerCx2InitializeDevice function](nf-sercx-sercx2initializedevice.md) | The SerCx2InitializeDevice method finishes initializing the framework device object for the serial controller. |
| [SerCx2InitializeDeviceInit function](nf-sercx-sercx2initializedeviceinit.md) | The SerCx2InitializeDeviceInit method enables version 2 of the serial framework extension (SerCx2) to register extension-specific properties with the driver framework during the creation of the framework device object for the serial controller. |
| [SerCx2PioReceiveCleanupTransactionComplete function](nf-sercx-sercx2pioreceivecleanuptransactioncomplete.md) | The SerCx2PioReceiveCleanupTransactionComplete method informs version 2 of the serial framework extension (SerCx2) that the serial controller driver has finished cleaning up the serial controller's hardware state after a PIO-receive transaction. |
| [SerCx2PioReceiveCreate function](nf-sercx-sercx2pioreceivecreate.md) | The SerCx2PioReceiveCreate method creates a PIO-receive object, which version 2 of the serial framework extension (SerCx2) uses to perform PIO-receive transactions. |
| [SerCx2PioReceiveInitializeTransactionComplete function](nf-sercx-sercx2pioreceiveinitializetransactioncomplete.md) | The SerCx2PioReceiveInitializeTransactionComplete method notifies version 2 of the serial framework extension (SerCx2) that the serial driver has finished initializing the serial controller hardware in preparation for a new PIO-receive transaction. |
| [SerCx2PioReceiveReady function](nf-sercx-sercx2pioreceiveready.md) | The SerCx2PioReceiveReady method notifies version 2 of the serial framework extension (SerCx2) that data is available to be read from the receive FIFO in the serial controller. |
| [SerCx2PioTransmitCleanupTransactionComplete function](nf-sercx-sercx2piotransmitcleanuptransactioncomplete.md) | The SerCx2PioTransmitCleanupTransactionComplete method notifies version 2 of the serial framework extension (SerCx2) that serial controller driver has finished cleaning up the serial controller's hardware state after a PIO-transmit transaction. |
| [SerCx2PioTransmitCreate function](nf-sercx-sercx2piotransmitcreate.md) | The SerCx2PioTransmitCreate method creates a PIO-transmit object, which version 2 of the serial framework extension (SerCx2) uses to perform PIO-transmit transactions. |
| [SerCx2PioTransmitDrainFifoComplete function](nf-sercx-sercx2piotransmitdrainfifocomplete.md) | The SerCx2PioTransmitDrainFifoComplete method notifies version 2 of the serial framework extension (SerCx2) that the serial controller driver has finished draining the data from the transmit FIFO in the serial controller hardware. |
| [SerCx2PioTransmitInitializeTransactionComplete function](nf-sercx-sercx2piotransmitinitializetransactioncomplete.md) | The SerCx2PioTransmitInitializeTransactionComplete method notifies version 2 of the serial framework extension (SerCx2) that the serial controller driver has finished initializing the serial controller hardware in preparation for a new PIO-transmit transaction. |
| [SerCx2PioTransmitPurgeFifoComplete function](nf-sercx-sercx2piotransmitpurgefifocomplete.md) | The SerCx2PioTransmitPurgeFifoComplete method notifies version 2 of the serial framework extension (SerCx2) that the serial controller driver has finished purging the data from the transmit FIFO in the serial controller hardware. |
| [SerCx2PioTransmitReady function](nf-sercx-sercx2piotransmitready.md) | The SerCx2PioTransmitReady method notifies version 2 of the serial framework extension (SerCx2) that the transmit FIFO in the serial controller hardware is ready to accept more data. |
| [SerCx2SaveReceiveFifoOnD0Exit function](nf-sercx-sercx2savereceivefifoond0exit.md) | The SerCx2SaveReceiveFifoOnD0Exit method informs version 2 of the serial framework extension (SerCx2) that the receive FIFO of the serial controller hardware contains data that should be saved before the serial controller enters a device low-power state. |
| [SerCx2SystemDmaReceiveCleanupTransactionComplete function](nf-sercx-sercx2systemdmareceivecleanuptransactioncomplete.md) | The SerCx2SystemDmaReceiveCleanupTransactionComplete method notifies version 2 of the serial framework extension (SerCx2) that the serial controller driver has finished cleaning up the serial controller's hardware state after a system-DMA-receive transaction. |
| [SerCx2SystemDmaReceiveCreate function](nf-sercx-sercx2systemdmareceivecreate.md) | The SerCx2SystemDmaReceiveCreate method creates a SerCx2 system-DMA-receive object, which version 2 of the serial framework extension (SerCx2) uses to perform system-DMA-receive transactions. |
| [SerCx2SystemDmaReceiveGetDmaEnabler function](nf-sercx-sercx2systemdmareceivegetdmaenabler.md) | The SerCx2SystemDmaReceiveGetDmaEnabler method gets the DMA enabler for the system DMA controller that is used for system-DMA-receive transactions. |
| [SerCx2SystemDmaReceiveInitializeTransactionComplete function](nf-sercx-sercx2systemdmareceiveinitializetransactioncomplete.md) | The SerCx2SystemDmaReceiveInitializeTransactionComplete method notifies version 2 of the serial framework extension (SerCx2) that the serial driver has finished initializing the serial controller hardware in preparation for a new system-DMA-receive transaction. |
| [SerCx2SystemDmaReceiveNewDataNotification function](nf-sercx-sercx2systemdmareceivenewdatanotification.md) | The SerCx2SystemDmaReceiveNewDataNotification method notifies version 2 of the serial framework extension (SerCx2) that data is available to be read from the receive FIFO in the serial controller hardware. |
| [SerCx2SystemDmaTransmitCleanupTransactionComplete function](nf-sercx-sercx2systemdmatransmitcleanuptransactioncomplete.md) | The SerCx2SystemDmaTransmitCleanupTransactionComplete method notifies version 2 of the serial framework extension (SerCx2) that the serial controller driver has finished cleaning up the serial controller's hardware state after a system-DMA-transmit transaction. |
| [SerCx2SystemDmaTransmitCreate function](nf-sercx-sercx2systemdmatransmitcreate.md) | The SerCx2SystemDmaTransmitCreate method creates a SerCx2 system-DMA-transmit object, which version 2 of the serial framework extension (SerCx2) uses to perform system-DMA-transmit transactions. |
| [SerCx2SystemDmaTransmitDrainFifoComplete function](nf-sercx-sercx2systemdmatransmitdrainfifocomplete.md) | The SerCx2SystemDmaTransmitDrainFifoComplete method notifies version 2 of the serial framework extension (SerCx2) that the serial controller driver has finished draining the data from the transmit FIFO in the serial controller hardware. |
| [SerCx2SystemDmaTransmitGetDmaEnabler function](nf-sercx-sercx2systemdmatransmitgetdmaenabler.md) | The SerCx2SystemDmaTransmitGetDmaEnabler method gets the DMA enabler for the system DMA controller that is used for system-DMA-transmit transactions. |
| [SerCx2SystemDmaTransmitInitializeTransactionComplete function](nf-sercx-sercx2systemdmatransmitinitializetransactioncomplete.md) | The SerCx2SystemDmaTransmitInitializeTransactionComplete method notifies version 2 of the serial framework extension (SerCx2) that the serial controller driver has finished initializing the serial controller hardware in preparation for a new system-DMA-transmit transaction. |
| [SerCx2SystemDmaTransmitPurgeFifoComplete function](nf-sercx-sercx2systemdmatransmitpurgefifocomplete.md) | The SerCx2SystemDmaTransmitPurgeFifoComplete method notifies version 2 of the serial framework extension (SerCx2) that the serial controller driver has finished purging the data from the transmit FIFO in the serial controller hardware. |
| [SerCxCompleteWait function](nf-sercx-sercxcompletewait.md) | The SerCxCompleteWait method notifies the serial framework extension (SerCx) that an event in the current wait mask has occurred. |
| [SerCxDeviceInitConfig function](nf-sercx-sercxdeviceinitconfig.md) | The SerCxDeviceInitConfig method is called by the serial controller driver to attach the serial framework extension (SerCx) to the I/O pipeline for a framework device object (FDO or PDO) that it is creating. |
| [SerCxGetActivity function](nf-sercx-sercxgetactivity.md) | The SerCxGetActivity method retrieves the status of pending work for the serial controller driver. |
| [SerCxGetConnectionParameters function](nf-sercx-sercxgetconnectionparameters.md) | The SerCxGetConnectionParameters method retrieves the connection parameters for the associated peripheral device. |
| [SerCxGetReadIntervalTimeout function](nf-sercx-sercxgetreadintervaltimeout.md) | The SerCxGetReadIntervalTimeout method returns the interval time-out value for a read (receive) operation. |
| [SerCxGetRingBufferUtilization function](nf-sercx-sercxgetringbufferutilization.md) | The SerCxGetRingBufferUtilization method enables the serial controller driver to determine how much of the type-ahead ring buffer is currently filled by data received from the serial port. |
| [SerCxGetWaitMask function](nf-sercx-sercxgetwaitmask.md) | The SerCxGetWaitMask method returns the event wait mask for the wait operation that is currently pending. |
| [SerCxInitialize function](nf-sercx-sercxinitialize.md) | The SerCxInitialize method completes the initialization of the serial framework extension (SerCx) after this driver creates the associated device object. |
| [SerCxProgressReceive function](nf-sercx-sercxprogressreceive.md) | The SerCxProgressReceive method reports the progress of the current read (receive) operation. |
| [SerCxProgressTransmit function](nf-sercx-sercxprogresstransmit.md) | The SerCxProgressTransmit method reports the progress of the current write (transmit) operation. |
| [SerCxRetrieveReceiveBuffer function](nf-sercx-sercxretrievereceivebuffer.md) | The SerCxRetrieveReceiveBuffer method obtains an input buffer into which data received from the serial port can be loaded. |
| [SerCxRetrieveReceiveMdl function](nf-sercx-sercxretrievereceivemdl.md) | The SerCxRetrieveReceiveMdl method retrieves the MDL that describes the buffer to use to receive the next block of input data. |
| [SerCxRetrieveTransmitBuffer function](nf-sercx-sercxretrievetransmitbuffer.md) | The SerCxRetrieveTransmitBuffer method obtains an output buffer that contains data that is ready to be transmitted to the serial port. |
| [SerCxRetrieveTransmitMdl function](nf-sercx-sercxretrievetransmitmdl.md) | The SerCxRetrieveTransmitMdl method retrieves the MDL that describes the buffer that contains the next block of output data to be transmitted. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [SERCX_BUFFER_DESCRIPTOR structure](ns-sercx-sercx_buffer_descriptor.md) | The SERCX_BUFFER_DESCRIPTOR structure describes a data buffer for a receive operation or transmit operation. |
| [_SERCX2_CONFIG structure](ns-sercx-_sercx2_config.md) | The SERCX2_CONFIG structure contains configuration information for version 2 of the serial framework extension (SerCx2). |
| [_SERCX2_CUSTOM_RECEIVE_CONFIG structure](ns-sercx-_sercx2_custom_receive_config.md) | The SERCX2_CUSTOM_RECEIVE_CONFIG structure contains information that version 2 of the serial framework extension (SerCx2) uses to configure a new custom-receive object. |
| [_SERCX2_CUSTOM_RECEIVE_TRANSACTION_CONFIG structure](ns-sercx-_sercx2_custom_receive_transaction_config.md) | The SERCX2_CUSTOM_RECEIVE_TRANSACTION_CONFIG structure contains information that version 2 of the serial framework extension (SerCx2) uses to configure a new custom-receive-transaction object. |
| [_SERCX2_CUSTOM_TRANSMIT_CONFIG structure](ns-sercx-_sercx2_custom_transmit_config.md) | The SERCX2_CUSTOM_TRANSMIT_CONFIG structure contains information that version 2 of the serial framework extension (SerCx2) uses to configure a new custom-transmit object. |
| [_SERCX2_CUSTOM_TRANSMIT_TRANSACTION_CONFIG structure](ns-sercx-_sercx2_custom_transmit_transaction_config.md) | The SERCX2_CUSTOM_TRANSMIT_TRANSACTION_CONFIG structure contains information that version 2 of the serial framework extension (SerCx2) uses to configure a new custom-transmit-transaction object. |
| [_SERCX2_PIO_RECEIVE_CONFIG structure](ns-sercx-_sercx2_pio_receive_config.md) | The SERCX2_PIO_RECEIVE_CONFIG structure contains information that version 2 of the serial framework extension (SerCx2) uses to configure a new PIO-receive object. |
| [_SERCX2_PIO_TRANSMIT_CONFIG structure](ns-sercx-_sercx2_pio_transmit_config.md) | The SERCX2_PIO_TRANSMIT_CONFIG structure contains information that version 2 of the serial framework extension (SerCx2) uses to configure a new PIO-transmit object. |
| [_SERCX2_SYSTEM_DMA_RECEIVE_CONFIG structure](ns-sercx-_sercx2_system_dma_receive_config.md) | The SERCX2_SYSTEM_DMA_RECEIVE_CONFIG structure contains information that version 2 of the serial framework extension (SerCx2) uses to configure a new system-DMA-receive object. |
| [_SERCX2_SYSTEM_DMA_TRANSMIT_CONFIG structure](ns-sercx-_sercx2_system_dma_transmit_config.md) | The SERCX2_SYSTEM_DMA_TRANSMIT_CONFIG structure contains information that version 2 of the serial framework extension (SerCx2) uses to configure a new system-DMA-transmit object. |
| [_SERCX_ACTIVITY structure](ns-sercx-_sercx_activity.md) | The SERCX_ACTIVITY structure contains a summary of work items that are ready for the serial controller driver to process. |
| [_SERCX_CONFIG structure](ns-sercx-_sercx_config.md) | The SERCX_CONFIG structure contains configuration information for the serial framework extension (SerCx). |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [_SERCX2_CUSTOM_RECEIVE_TRANSACTION_PROGRESS enumeration](ne-sercx-_sercx2_custom_receive_transaction_progress.md) | The SERCX2_CUSTOM_RECEIVE_TRANSACTION_PROGRESS enumeration defines constants that indicate whether process is being made toward completing a custom-receive transaction. |
| [_SERCX2_TRANSACTION_TYPE enumeration](ne-sercx-_sercx2_transaction_type.md) | The SERCX2_TRANSACTION_TYPE enumeration defines constants that indicate the type of data-transfer mechanism to use to perform an I/O transaction. |
| [_SERCX_STATUS enumeration](ne-sercx-_sercx_status.md) | The SERCX_STATUS enumeration indicates the status of a serial receive or transmit operation. |
