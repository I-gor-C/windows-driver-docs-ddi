---
UID: NA:spbcx
---

# Spbcx.h header

## -description

This header is used by SPB. For more information, see
- [SPB](../_SPB/index.md)

Spbcx.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [SPB_CONNECTION_PARAMETERS_INIT function](nf-spbcx-spb_connection_parameters_init.md) | The SPB_CONNECTION_PARAMETERS_INIT function initializes an SPB_CONNECTION_PARAMETERS structure. |
| [SPB_CONTROLLER_CONFIG_INIT function](nf-spbcx-spb_controller_config_init.md) | The SPB_CONTROLLER_CONFIG_INIT function initializes an SPB_CONTROLLER_CONFIG structure. |
| [SPB_REQUEST_PARAMETERS_INIT function](nf-spbcx-spb_request_parameters_init.md) | The SPB_REQUEST_PARAMETERS_INIT function initializes an SPB_REQUEST_PARAMETERS structure. |
| [SPB_TRANSFER_DESCRIPTOR_INIT function](nf-spbcx-spb_transfer_descriptor_init.md) | The SPB_TRANSFER_DESCRIPTOR_INIT function initializes an SPB_TRANSFER_DESCRIPTOR structure. |
| [SpbControllerSetIoOtherCallback function](nf-spbcx-spbcontrollersetioothercallback.md) | The SpbControllerSetIoOtherCallback method registers an SPB controller driver's EvtSpbControllerIoOther callback function. |
| [SpbControllerSetRequestAttributes function](nf-spbcx-spbcontrollersetrequestattributes.md) | The SpbControllerSetRequestAttributes method sets object attributes that will be used for all SPBREQUEST objects that the SPB framework extension (SpbCx) delivers to the SPB controller driver. |
| [SpbControllerSetTargetAttributes function](nf-spbcx-spbcontrollersettargetattributes.md) | The SpbControllerSetTargetAttributes method sets object attributes that will be used for all SPBTARGET objects that the SPB framework extension (SpbCx) delivers to the SPB controller driver. |
| [SpbDeviceInitConfig function](nf-spbcx-spbdeviceinitconfig.md) | The SpbDeviceInitConfig method attaches the SPB framework extension (SpbCx) to the I/O-request chain for a WDFDEVICE (FDO or PDO) object that is to be created. |
| [SpbDeviceInitialize function](nf-spbcx-spbdeviceinitialize.md) | The SpbDeviceInitialize method completes the initialization of the SPB controller driver after this driver creates the associated device object. |
| [SpbRequestCaptureIoOtherTransferList function](nf-spbcx-spbrequestcaptureioothertransferlist.md) | The SpbRequestCaptureIoOtherTransferList method retrieves the SPB_TRANSFER_LIST structure in the input buffer of the custom IOCTL request. |
| [SpbRequestComplete function](nf-spbcx-spbrequestcomplete.md) | The SpbRequestComplete method completes an I/O request and supplies a completion status. |
| [SpbRequestGetController function](nf-spbcx-spbrequestgetcontroller.md) | The SpbRequestGetController method returns the WDFDEVICE handle to the device object for the SPB controller that the specified I/O request was sent to. |
| [SpbRequestGetParameters function](nf-spbcx-spbrequestgetparameters.md) | The SpbRequestGetParameters method retrieves a set of SPB-specific parameter values from an I/O request. |
| [SpbRequestGetTarget function](nf-spbcx-spbrequestgettarget.md) | The SpbRequestGetTarget method retrieves the SPBTARGET handle from the specified I/O request. |
| [SpbRequestGetTransferParameters function](nf-spbcx-spbrequestgettransferparameters.md) | The SpbRequestGetTransferParameters method retrieves the transfer parameters for an individual transfer in an I/O transfer sequence. |
| [SpbTargetGetConnectionParameters function](nf-spbcx-spbtargetgetconnectionparameters.md) | The SpbTargetGetConnectionParameters method retrieves the connection parameters for a target device on the bus. |
| [SpbTargetGetFileObject function](nf-spbcx-spbtargetgetfileobject.md) | The SpbTargetGetFileObject method accepts, as an input parameter, an SPBTARGET handle to an open target device, and returns a WDFFILEOBJECT handle to this target. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [SPB_TRANSFER_DESCRIPTOR structure](ns-spbcx-spb_transfer_descriptor.md) | The SPB_TRANSFER_DESCRIPTOR structure describes a single transfer in an I/O transfer sequence. |
| [_SPB_CONNECTION_PARAMETERS structure](ns-spbcx-_spb_connection_parameters.md) | The SPB_CONNECTION_PARAMETERS structure contains the connection parameters for a target device on a simple peripheral bus. |
| [_SPB_CONTROLLER_CONFIG structure](ns-spbcx-_spb_controller_config.md) | The SPB_CONTROLLER_CONFIG structure contains the configuration settings for an SPB controller driver. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [_SPB_REQUEST_SEQUENCE_POSITION enumeration](ne-spbcx-_spb_request_sequence_position.md) | The SPB_REQUEST_SEQUENCE_POSITION enumeration indicates the position of an I/O request in the list of transfers for an I/O transfer sequence. |
| [_SPB_REQUEST_TYPE enumeration](ne-spbcx-_spb_request_type.md) | The SPB_REQUEST_TYPE enumeration specifies the type of SPB operation that a client is requesting. |
