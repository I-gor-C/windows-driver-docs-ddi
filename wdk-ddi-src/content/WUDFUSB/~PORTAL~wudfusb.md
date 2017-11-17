# Declarations in the wudfusb header
This header Wudfusb contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [IWDFUsbInterface::RetrieveUsbPipeObject method](nf-wudfusb-iwdfusbinterface-retrieveusbpipeobject.md) | The RetrieveUsbPipeObject method retrieves a USB pipe object for the specified pipe index. |
| [IWDFUsbTargetPipe::IsInEndPoint method](nf-wudfusb-iwdfusbtargetpipe-isinendpoint.md) | The IsInEndPoint method determines whether a USB pipe (endpoint) is an IN pipe. |
| [IWDFUsbInterface::GetInterfaceDescriptor method](nf-wudfusb-iwdfusbinterface-getinterfacedescriptor.md) | The GetInterfaceDescriptor method retrieves a descriptor for a USB interface. |
| [IWDFUsbTargetDevice::GetWinUsbHandle method](nf-wudfusb-iwdfusbtargetdevice-getwinusbhandle.md) | The GetWinUsbHandle method retrieves the WinUsb interface handle that is associated with a I/O target device object. |
| [IWDFUsbTargetPipe::Reset method](nf-wudfusb-iwdfusbtargetpipe-reset.md) | The Reset method resets the data toggle and clears the stall condition on a USB pipe. |
| [IUsbTargetPipeContinuousReaderCallbackReadersFailed::OnReaderFailure method](nf-wudfusb-iusbtargetpipecontinuousreadercallbackreadersfailed-onreaderfailure.md) | A driver's OnReaderFailure event callback function informs the driver that a continuous reader has reported an error while processing a read request. |
| [IWDFUsbTargetPipe::Flush method](nf-wudfusb-iwdfusbtargetpipe-flush.md) | The Flush method discards any data that WinUsb saved when the device returned more data than the client requested. |
| [IWDFUsbTargetPipe::GetInformation method](nf-wudfusb-iwdfusbtargetpipe-getinformation.md) | The GetInformation method retrieves information about a USB pipe (endpoint). |
| [IWDFUsbRequestCompletionParams::GetCompletedUsbRequestType method](nf-wudfusb-iwdfusbrequestcompletionparams-getcompletedusbrequesttype.md) | The GetCompletedUsbRequestType method retrieves the type of operation that the request to be completed contains. |
| [IWDFUsbRequestCompletionParams::GetDeviceControlTransferParameters method](nf-wudfusb-iwdfusbrequestcompletionparams-getdevicecontroltransferparameters.md) | The GetDeviceControlTransferParameters method retrieves parameters that are associated with the completion of a device I/O control request. |
| [IWDFUsbTargetPipe::SetPipePolicy method](nf-wudfusb-iwdfusbtargetpipe-setpipepolicy.md) | The SetPipePolicy method sets the WinUsb pipe policy. |
| [IWDFUsbTargetPipe::GetType method](nf-wudfusb-iwdfusbtargetpipe-gettype.md) | The GetType method retrieves the type of a USB pipe. |
| [IWDFUsbRequestCompletionParams::GetPipeReadParameters method](nf-wudfusb-iwdfusbrequestcompletionparams-getpipereadparameters.md) | The GetPipeReadParameters method retrieves parameters that are associated with the completion of a read request. |
| [IWDFUsbTargetDevice::GetNumInterfaces method](nf-wudfusb-iwdfusbtargetdevice-getnuminterfaces.md) | The GetNumInterfaces method retrieves the number of USB interfaces for the USB device. |
| [IWDFUsbTargetPipe::IsOutEndPoint method](nf-wudfusb-iwdfusbtargetpipe-isoutendpoint.md) | The IsOutEndPoint method determines whether a USB pipe (endpoint) is an OUT pipe. |
| [IWDFUsbInterface::GetConfiguredSettingIndex method](nf-wudfusb-iwdfusbinterface-getconfiguredsettingindex.md) | The GetConfiguredSettingIndex method retrieves the current setting index for a USB interface. |
| [IWDFUsbTargetDevice::RetrievePowerPolicy method](nf-wudfusb-iwdfusbtargetdevice-retrievepowerpolicy.md) | The RetrievePowerPolicy method retrieves a WinUsb power policy. |
| [IWDFUsbTargetDevice::RetrieveUsbInterface method](nf-wudfusb-iwdfusbtargetdevice-retrieveusbinterface.md) | The RetrieveUsbInterface method retrieves the specified USB interface for a USB device. |
| [IWDFUsbInterface::GetNumEndPoints method](nf-wudfusb-iwdfusbinterface-getnumendpoints.md) | The GetNumEndPoints method retrieves the number of endpoints (pipes) on a USB interface. |
| [IUsbTargetPipeContinuousReaderCallbackReadComplete::OnReaderCompletion method](nf-wudfusb-iusbtargetpipecontinuousreadercallbackreadcomplete-onreadercompletion.md) | A driver's OnReaderCompletion event callback function informs the driver that a continuous reader has successfully completed a read request. |
| [IWDFUsbTargetDevice::RetrieveDeviceInformation method](nf-wudfusb-iwdfusbtargetdevice-retrievedeviceinformation.md) | The RetrieveDeviceInformation method retrieves device information of the specified type. |
| [IWDFUsbInterface::SelectSetting method](nf-wudfusb-iwdfusbinterface-selectsetting.md) | The SelectSetting method selects the specified alternate setting on a USB interface. |
| [IWDFUsbTargetDevice::RetrieveDescriptor method](nf-wudfusb-iwdfusbtargetdevice-retrievedescriptor.md) | The RetrieveDescriptor method retrieves a USB descriptor, which can describe a device, configuration, or string. |
| [IWDFUsbInterface::GetWinUsbHandle method](nf-wudfusb-iwdfusbinterface-getwinusbhandle~r1.md) | TBD |
| [IWDFUsbTargetPipe2::ConfigureContinuousReader method](nf-wudfusb-iwdfusbtargetpipe2-configurecontinuousreader.md) | The ConfigureContinuousReader method configures the framework to continuously read from a USB pipe. |
| [IWDFUsbTargetPipe::RetrievePipePolicy method](nf-wudfusb-iwdfusbtargetpipe-retrievepipepolicy.md) | The RetrievePipePolicy method retrieves a WinUsb pipe policy. |
| [IWDFUsbTargetDevice::SetPowerPolicy method](nf-wudfusb-iwdfusbtargetdevice-setpowerpolicy.md) | The SetPowerPolicy method sets the WinUsb power policy. |
| [IWDFUsbTargetPipe::Abort method](nf-wudfusb-iwdfusbtargetpipe-abort.md) | The Abort method aborts all pending transfers on a USB pipe. |
| [IWDFUsbInterface::GetWinUsbHandle method](nf-wudfusb-iwdfusbinterface-getwinusbhandle.md) | The GetWinUsbHandle method retrieves the WinUsb interface handle that is associated with a USB interface. |
| [IWDFUsbRequestCompletionParams::GetPipeWriteParameters method](nf-wudfusb-iwdfusbrequestcompletionparams-getpipewriteparameters.md) | The GetPipeWriteParameters method retrieves parameters that are associated with the completion of a write request. |
| [IWDFUsbInterface::GetInterfaceNumber method](nf-wudfusb-iwdfusbinterface-getinterfacenumber.md) | The GetInterfaceNumber method retrieves the index of a USB interface. |
| [IWDFUsbTargetFactory::CreateUsbTargetDevice method](nf-wudfusb-iwdfusbtargetfactory-createusbtargetdevice.md) | The CreateUsbTargetDevice method creates a USB device object that is also an I/O target. |
| [IWDFUsbTargetDevice::FormatRequestForControlTransfer method](nf-wudfusb-iwdfusbtargetdevice-formatrequestforcontroltransfer.md) | The FormatRequestForControlTransfer method formats an I/O request object for a USB control transfer. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WUDFUSB structure](ns-wudfusb-wudfusb~r1.md) | TBD |
| [IWDFUsbTargetDeviceVtbl structure](ns-wudfusb-iwdfusbtargetdevicevtbl.md) | TBD |
| [IUsbTargetPipeContinuousReaderCallbackReadersFailedVtbl structure](ns-wudfusb-iusbtargetpipecontinuousreadercallbackreadersfailedvtbl.md) | TBD |
| [IWDFUsbTargetPipeVtbl structure](ns-wudfusb-iwdfusbtargetpipevtbl.md) | TBD |
| [IWDFUsbInterfaceVtbl structure](ns-wudfusb-iwdfusbinterfacevtbl.md) | TBD |
| [IWDFUsbTargetFactoryVtbl structure](ns-wudfusb-iwdfusbtargetfactoryvtbl.md) | TBD |
| [IUsbTargetPipeContinuousReaderCallbackReadCompleteVtbl structure](ns-wudfusb-iusbtargetpipecontinuousreadercallbackreadcompletevtbl.md) | TBD |
| [WUDFUSB structure](ns-wudfusb-wudfusb.md) | TBD |
| [IWDFUsbTargetPipe2Vtbl structure](ns-wudfusb-iwdfusbtargetpipe2vtbl.md) | TBD |
| [IWDFUsbRequestCompletionParamsVtbl structure](ns-wudfusb-iwdfusbrequestcompletionparamsvtbl.md) | TBD |
Interface

| Title        | Description    |
| ------------- |:-------------:|
| [IWDFUsbInterface interface](nn-wudfusb-iwdfusbinterface~r1.md) | The IWDFUsbInterface interface exposes a USB interface that a USB device exposes. |
| [IUsbTargetPipeContinuousReaderCallbackReadComplete interface](nn-wudfusb-iusbtargetpipecontinuousreadercallbackreadcomplete~r1.md) | IUsbTargetPipeContinuousReaderCallbackReadComplete is a driver-supplied interface. |
| [IUsbTargetPipeContinuousReaderCallbackReadersFailed interface](nn-wudfusb-iusbtargetpipecontinuousreadercallbackreadersfailed.md) | IUsbTargetPipeContinuousReaderCallbackReadersFailed is a driver-supplied interface. |
| [IWDFUsbInterface interface](nn-wudfusb-iwdfusbinterface.md) | The IWDFUsbInterface interface exposes a USB interface that a USB device exposes. |
| [IWDFUsbTargetPipe interface](nn-wudfusb-iwdfusbtargetpipe.md) | The IWDFUsbTargetPipe interface exposes a USB pipe (endpoint), which is also an I/O target. |
| [IWDFUsbTargetPipe interface](nn-wudfusb-iwdfusbtargetpipe~r1.md) | The IWDFUsbTargetPipe interface exposes a USB pipe (endpoint), which is also an I/O target. |
| [IWDFUsbRequestCompletionParams interface](nn-wudfusb-iwdfusbrequestcompletionparams~r1.md) | The IWDFUsbRequestCompletionParams interface exposes the parameters object for the completion of a USB request object. The parameters object is primarily required for asynchronous I/O and layered drivers. |
| [IWDFUsbRequestCompletionParams interface](nn-wudfusb-iwdfusbrequestcompletionparams.md) | The IWDFUsbRequestCompletionParams interface exposes the parameters object for the completion of a USB request object. The parameters object is primarily required for asynchronous I/O and layered drivers. |
| [IWDFUsbTargetFactory interface](nn-wudfusb-iwdfusbtargetfactory.md) | The IWDFUsbTargetFactory interface is a factory interface that is used to create a USB target device object. |
| [IWDFUsbTargetDevice interface](nn-wudfusb-iwdfusbtargetdevice~r1.md) | The IWDFUsbTargetDevice interface exposes a USB device I/O target object. |
| [IWDFUsbTargetDevice interface](nn-wudfusb-iwdfusbtargetdevice.md) | The IWDFUsbTargetDevice interface exposes a USB device I/O target object. |
| [IWDFUsbTargetPipe2 interface](nn-wudfusb-iwdfusbtargetpipe2.md) | The IWDFUsbTargetPipe2 interface exposes a USB pipe (endpoint), which is also an I/O target. |
| [IUsbTargetPipeContinuousReaderCallbackReadersFailed interface](nn-wudfusb-iusbtargetpipecontinuousreadercallbackreadersfailed~r1.md) | IUsbTargetPipeContinuousReaderCallbackReadersFailed is a driver-supplied interface. |
| [IUsbTargetPipeContinuousReaderCallbackReadComplete interface](nn-wudfusb-iusbtargetpipecontinuousreadercallbackreadcomplete.md) | IUsbTargetPipeContinuousReaderCallbackReadComplete is a driver-supplied interface. |
| [IWDFUsbTargetFactory interface](nn-wudfusb-iwdfusbtargetfactory~r1.md) | The IWDFUsbTargetFactory interface is a factory interface that is used to create a USB target device object. |
| [IWDFUsbTargetPipe2 interface](nn-wudfusb-iwdfusbtargetpipe2~r1.md) | The IWDFUsbTargetPipe2 interface exposes a USB pipe (endpoint), which is also an I/O target. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_USB_REQUEST_TYPE enumeration](ne-wudfusb--wdf-usb-request-type~r1.md) | The WDF_USB_REQUEST_TYPE enumeration contains values that identify a type of USB request object. |
| [WDF_USB_REQUEST_TYPE enumeration](ne-wudfusb--wdf-usb-request-type.md) | The WDF_USB_REQUEST_TYPE enumeration contains values that identify a type of USB request object. |

This header is used in these topics:

- [wdf](..content/_wdf)
