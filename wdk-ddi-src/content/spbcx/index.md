---
UID: NA:spbcx
ms.assetid: 6b009b60-06dc-3225-88b1-4c355dadc70e
ms.author: windowsdriverdev
ms.date: 01/18/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# spbcx.h header



spbcx.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [EVT_SPB_CONTROLLER_LOCK](nc-spbcx-evt_spb_controller_lock.md) | An SPB controller driver's EvtSpbControllerLock event callback function locks the SPB controller for accesses of a single target device on the bus. |
| [EVT_SPB_CONTROLLER_OTHER](nc-spbcx-evt_spb_controller_other.md) | An SPB controller driver's EvtSpbControllerIoOther event callback function handles device I/O control requests that are not handled by other event callback functions or by the SPB framework extension (SpbCx). |
| [EVT_SPB_CONTROLLER_READ](nc-spbcx-evt_spb_controller_read.md) | An SPB controller driver's EvtSpbControllerIoRead event callback function reads data from the specified target device into the buffers that are supplied with the read request. |
| [EVT_SPB_CONTROLLER_SEQUENCE](nc-spbcx-evt_spb_controller_sequence.md) | An SPB controller driver's EvtSpbControllerIoSequence event callback function performs a sequence of data transfers between the specified target device and the buffers that are supplied with the sequence request. |
| [EVT_SPB_CONTROLLER_UNLOCK](nc-spbcx-evt_spb_controller_unlock.md) | An SPB controller driver's EvtSpbControllerUnlock event callback function unlocks the SPB controller, which was locked by a previous call to the EvtSpbControllerLock event callback function. |
| [EVT_SPB_CONTROLLER_WRITE](nc-spbcx-evt_spb_controller_write.md) | An SPB controller driver's EvtSpbControllerIoWrite event callback function writes data to the specified target device from the buffers that are supplied with the write request. |
| [EVT_SPB_TARGET_CONNECT](nc-spbcx-evt_spb_target_connect.md) | An SPB controller driver's EvtSpbTargetConnect event callback function opens a connection to a target device on the bus. |
| [EVT_SPB_TARGET_DISCONNECT](nc-spbcx-evt_spb_target_disconnect.md) | An SPB controller driver's EvtSpbTargetDisconnect event callback function closes a connection to a target device that was previously opened by a call to the driver's EvtSpbTargetConnect event callback function. |
| [SPB_CONNECTION_PARAMETERS_INIT](nf-spbcx-spb_connection_parameters_init.md) | The SPB_CONNECTION_PARAMETERS_INIT function initializes an SPB_CONNECTION_PARAMETERS structure. |
| [SPB_CONTROLLER_CONFIG_INIT](nf-spbcx-spb_controller_config_init.md) | The SPB_CONTROLLER_CONFIG_INIT function initializes an SPB_CONTROLLER_CONFIG structure. |
| [SPB_REQUEST_PARAMETERS_INIT](nf-spbcx-spb_request_parameters_init.md) | The SPB_REQUEST_PARAMETERS_INIT function initializes an SPB_REQUEST_PARAMETERS structure. |
| [SPB_TRANSFER_DESCRIPTOR_INIT](nf-spbcx-spb_transfer_descriptor_init.md) | The SPB_TRANSFER_DESCRIPTOR_INIT function initializes an SPB_TRANSFER_DESCRIPTOR structure. |
| [SpbControllerSetIoOtherCallback](nf-spbcx-spbcontrollersetioothercallback.md) | The SpbControllerSetIoOtherCallback method registers an SPB controller driver's EvtSpbControllerIoOther callback function. |
| [SpbControllerSetRequestAttributes](nf-spbcx-spbcontrollersetrequestattributes.md) | The SpbControllerSetRequestAttributes method sets object attributes that will be used for all SPBREQUEST objects that the SPB framework extension (SpbCx) delivers to the SPB controller driver. |
| [SpbControllerSetTargetAttributes](nf-spbcx-spbcontrollersettargetattributes.md) | The SpbControllerSetTargetAttributes method sets object attributes that will be used for all SPBTARGET objects that the SPB framework extension (SpbCx) delivers to the SPB controller driver. |
| [SpbDeviceInitConfig](nf-spbcx-spbdeviceinitconfig.md) | The SpbDeviceInitConfig method attaches the SPB framework extension (SpbCx) to the I/O-request chain for a WDFDEVICE (FDO or PDO) object that is to be created. |
| [SpbDeviceInitialize](nf-spbcx-spbdeviceinitialize.md) | The SpbDeviceInitialize method completes the initialization of the SPB controller driver after this driver creates the associated device object. |
| [SpbRequestCaptureIoOtherTransferList](nf-spbcx-spbrequestcaptureioothertransferlist.md) | The SpbRequestCaptureIoOtherTransferList method retrieves the SPB_TRANSFER_LIST structure in the input buffer of the custom IOCTL request. |
| [SpbRequestComplete](nf-spbcx-spbrequestcomplete.md) | The SpbRequestComplete method completes an I/O request and supplies a completion status. |
| [SpbRequestGetController](nf-spbcx-spbrequestgetcontroller.md) | The SpbRequestGetController method returns the WDFDEVICE handle to the device object for the SPB controller that the specified I/O request was sent to. |
| [SpbRequestGetParameters](nf-spbcx-spbrequestgetparameters.md) | The SpbRequestGetParameters method retrieves a set of SPB-specific parameter values from an I/O request. |
| [SpbRequestGetTarget](nf-spbcx-spbrequestgettarget.md) | The SpbRequestGetTarget method retrieves the SPBTARGET handle from the specified I/O request. |
| [SpbRequestGetTransferParameters](nf-spbcx-spbrequestgettransferparameters.md) | The SpbRequestGetTransferParameters method retrieves the transfer parameters for an individual transfer in an I/O transfer sequence. |
| [SpbTargetGetConnectionParameters](nf-spbcx-spbtargetgetconnectionparameters.md) | The SpbTargetGetConnectionParameters method retrieves the connection parameters for a target device on the bus. |
| [SpbTargetGetFileObject](nf-spbcx-spbtargetgetfileobject.md) | The SpbTargetGetFileObject method accepts, as an input parameter, an SPBTARGET handle to an open target device, and returns a WDFFILEOBJECT handle to this target. |



## Structures
| Title | Description |
| ---- |:---- |
| [_SPB_CONNECTION_PARAMETERS](ns-spbcx-_spb_connection_parameters.md) | The SPB_CONNECTION_PARAMETERS structure contains the connection parameters for a target device on a simple peripheral bus. |
| [_SPB_CONTROLLER_CONFIG](ns-spbcx-_spb_controller_config.md) | The SPB_CONTROLLER_CONFIG structure contains the configuration settings for an SPB controller driver. |
| [SPB_TRANSFER_DESCRIPTOR](ns-spbcx-spb_transfer_descriptor.md) | The SPB_TRANSFER_DESCRIPTOR structure describes a single transfer in an I/O transfer sequence. |


## Enumerations
| Title | Description |
| ---- |:---- |
| [_SPB_REQUEST_SEQUENCE_POSITION](ne-spbcx-_spb_request_sequence_position.md) | The SPB_REQUEST_SEQUENCE_POSITION enumeration indicates the position of an I/O request in the list of transfers for an I/O transfer sequence. |
| [_SPB_REQUEST_TYPE](ne-spbcx-_spb_request_type.md) | The SPB_REQUEST_TYPE enumeration specifies the type of SPB operation that a client is requesting. |