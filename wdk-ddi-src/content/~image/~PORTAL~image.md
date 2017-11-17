# Declarations in the image technology
This technology  contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [PTP_VENDOR_DATA_IN structure](..\ptpusd\ns-ptpusd--ptp-vendor-data-in.md) | The PTP_VENDOR_DATA_IN structure contains information about an arbitrary command that an application issues to the device. |
| [PTP_VENDOR_DATA_OUT structure](..\ptpusd\ns-ptpusd--ptp-vendor-data-out.md) | The PTP_VENDOR_DATA_OUT structure contains information that the device sends to an application, in response to a command the application issued to the device. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [SCSISCAN_CMD structure](..\scsiscan\ns-scsiscan--scsiscan-cmd.md) | The SCSISCAN_CMD structure is used as a parameter to DeviceIoControl, when the specified I/O control code is IOCTL_SCSISCAN_CMD. |
| [SCSISCAN_INFO structure](..\scsiscan\ns-scsiscan--scsiscan-info.md) | The SCSISCAN_INFO structure is used as a parameter to DeviceIoControl (described in the Microsoft Windows SDK documentation), when the specified I/O control code is IOCTL_SCSISCAN_GET_INFO. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [IStiDevice::RawReadData method](..\sti\nf-sti-istidevice-rawreaddata.md) | The IStiDevice |
| [IStiDevice::GetLastNotificationData method](..\sti\nf-sti-istidevice-getlastnotificationdata.md) | The IStiDevice |
| [IStiDevice::GetLastErrorInfo method](..\sti\nf-sti-istidevice-getlasterrorinfo.md) | The IStiDevice |
| [IStiDevice::GetStatus method](..\sti\nf-sti-istidevice-getstatus.md) | The IStiDevice |
| [IStiDevice::GetCapabilities method](..\sti\nf-sti-istidevice-getcapabilities.md) | The IStiDevice |
| [IStiDevice::RawReadCommand method](..\sti\nf-sti-istidevice-rawreadcommand.md) | The IStiDevice |
| [IStiDevice::UnLockDevice method](..\sti\nf-sti-istidevice-unlockdevice.md) | The IStiDevice |
| [IStiDevice::UnSubscribe method](..\sti\nf-sti-istidevice-unsubscribe.md) | The IStiDevice |
| [IStiDevice::Escape method](..\sti\nf-sti-istidevice-escape.md) | The IStiDevice |
| [IStiDevice::Initialize method](..\sti\nf-sti-istidevice-initialize.md) | The IStiDevice |
| [IStiDevice::RawWriteCommand method](..\sti\nf-sti-istidevice-rawwritecommand.md) | The IStiDevice |
| [IStiDevice::Subscribe method](..\sti\nf-sti-istidevice-subscribe.md) | The IStiDevice |
| [IStiDevice::Release method](..\sti\nf-sti-istidevice-release.md) | The IStiDevice |
| [IStiDevice::Diagnostic method](..\sti\nf-sti-istidevice-diagnostic.md) | The IStiDevice |
| [IStiDevice::DeviceReset method](..\sti\nf-sti-istidevice-devicereset.md) | The IStiDevice |
| [IStiDevice::LockDevice method](..\sti\nf-sti-istidevice-lockdevice.md) | The IStiDevice |
| [IStiDevice::GetLastError method](..\sti\nf-sti-istidevice-getlasterror.md) | The IStiDevice |
| [IStiDevice::RawWriteData method](..\sti\nf-sti-istidevice-rawwritedata.md) | The IStiDevice |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [STINOTIFY structure](..\sti\ns-sti--stinotify.md) | The STINOTIFY structure is used as a parameter to the IStillImage |
| [STISUBSCRIBE structure](..\sti\ns-sti--stisubscribe.md) | The STISUBSCRIBE structure is used as a parameter for the IStiDevice |
| [STI_DEV_CAPS structure](..\sti\ns-sti--sti-dev-caps.md) | The STI_DEV_CAPS structure is used as a parameter to the IStiDevice |
| [STI_DEVICE_STATUS structure](..\sti\ns-sti--sti-device-status.md) | The STI_DEVICE_STATUS structure is used as a parameter to the IStiDevice |
| [STI_DIAG structure](..\sti\ns-sti--sti-diag.md) | The STI_DIAG structure is used as a parameter to the IStiDevice |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [IStiUSD::UnLockDevice method](..\stiusd\nf-stiusd-istiusd-unlockdevice.md) | A still image minidriver's IStiUSD |
| [IStiUSD::GetLastError method](..\stiusd\nf-stiusd-istiusd-getlasterror.md) | The IStiUSD |
| [IStiUSD::Initialize method](..\stiusd\nf-stiusd-istiusd-initialize.md) | A still image minidriver's IStiUSD |
| [IStiUSD::DeviceReset method](..\stiusd\nf-stiusd-istiusd-devicereset.md) | A still image minidriver's IStiUSD |
| [IStiUSD::GetLastErrorInfo method](..\stiusd\nf-stiusd-istiusd-getlasterrorinfo.md) | A still image minidriver's IStiUSD |
| [IStiUSD::RawWriteData method](..\stiusd\nf-stiusd-istiusd-rawwritedata.md) | A still image minidriver's IStiUSD |
| [IStiDeviceControl::RawDeviceControl method](..\stiusd\nf-stiusd-istidevicecontrol-rawdevicecontrol.md) | This topic describes the RawDeviceControl method. |
| [IStiUSD::GetStatus method](..\stiusd\nf-stiusd-istiusd-getstatus.md) | A still image minidriver's IStiUSD |
| [IStiDeviceControl::AddRef method](..\stiusd\nf-stiusd-istidevicecontrol-addref.md) | The IStiDeviceControl |
| [IStiUSD::RawReadCommand method](..\stiusd\nf-stiusd-istiusd-rawreadcommand.md) | A still image minidriver's IStiUSD |
| [IStiDeviceControl::WriteToErrorLog method](..\stiusd\nf-stiusd-istidevicecontrol-writetoerrorlog.md) | The IStiDeviceControl |
| [IStiUSD::GetCapabilities method](..\stiusd\nf-stiusd-istiusd-getcapabilities.md) | A still image minidriver's IStiUSD |
| [IStiUSD::Diagnostic method](..\stiusd\nf-stiusd-istiusd-diagnostic.md) | A still image minidriver's IStiUSD |
| [IStiDeviceControl::GetMyDeviceOpenMode method](..\stiusd\nf-stiusd-istidevicecontrol-getmydeviceopenmode.md) | The IStiDeviceControl |
| [IStiUSD::RawWriteCommand method](..\stiusd\nf-stiusd-istiusd-rawwritecommand.md) | A still image minidriver's IStiDevice |
| [IStiUSD::Escape method](..\stiusd\nf-stiusd-istiusd-escape.md) | A still image minidriver's IStiUSD |
| [IStiUSD::RawReadData method](..\stiusd\nf-stiusd-istiusd-rawreaddata.md) | A still image minidriver's IStiUSD |
| [IStiUSD::LockDevice method](..\stiusd\nf-stiusd-istiusd-lockdevice.md) | A still image minidriver's IStiUSD |
| [IStiDeviceControl::GetMyDeviceHandle method](..\stiusd\nf-stiusd-istidevicecontrol-getmydevicehandle.md) | This topic describes the GetMyDeviceHandle method. |
| [IStiUSD::SetNotificationHandle method](..\stiusd\nf-stiusd-istiusd-setnotificationhandle.md) | A still image minidriver's IStiUSD |
| [IStiDeviceControl::Release method](..\stiusd\nf-stiusd-istidevicecontrol-release.md) | The IStiDeviceControl |
| [IStiUSD::GetNotificationData method](..\stiusd\nf-stiusd-istiusd-getnotificationdata.md) | A still image minidriver's IStiUSD |
| [IStiDeviceControl::GetMyDevicePortName method](..\stiusd\nf-stiusd-istidevicecontrol-getmydeviceportname.md) | The IStiDeviceControl |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [STI_USD_CAPS structure](..\stiusd\ns-stiusd--sti-usd-caps.md) | The STI_USD_CAPS structure is used as a parameter for the IStiUSD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [DEVICE_DESCRIPTOR structure](..\usbscan\ns-usbscan--device-descriptor.md) | The DEVICE_DESCRIPTOR structure is used as a parameter to DeviceIoControl, when the specified I/O control code is IOCTL_GET_DEVICE_DESCRIPTOR. |
| [USBSCAN_PIPE_CONFIGURATION structure](..\usbscan\ns-usbscan--usbscan-pipe-configuration.md) | The USBSCAN_PIPE_CONFIGURATION structure is used as a parameter to DeviceIoControl, when the specified I/O control code is IOCTL_GET_PIPE_CONFIGURATION. |
| [IO_BLOCK structure](..\usbscan\ns-usbscan--io-block.md) | The IO_BLOCK structure is used as a parameter to DeviceIoControl, when the specified I/O control code is IOCTL_READ_REGISTERS or IOCTL_WRITE_REGISTERS. |
| [DRV_VERSION structure](..\usbscan\ns-usbscan--drv-version.md) | The DRV_VERSION structure is used as a parameter to DeviceIoControl, when the specified I/O control code is IOCTL_GET_VERSION. |
| [IO_BLOCK_EX structure](..\usbscan\ns-usbscan--io-block-ex.md) | The IO_BLOCK_EX structure is used as a parameter to DeviceIoControl, when the specified I/O control code is IOCTL_SEND_USB_REQUEST. |
| [USBSCAN_PIPE_INFORMATION structure](..\usbscan\ns-usbscan--usbscan-pipe-information.md) | The USBSCAN_PIPE_INFORMATION structure is used to describe a USB transfer pipe for a still image device. An array of USBSCAN_PIPE_INFORMATION structures is supplied within a USBSCAN_PIPE_CONFIGURATION structure. |
| [USBSCAN_GET_DESCRIPTOR structure](..\usbscan\ns-usbscan--usbscan-get-descriptor.md) | The USBSCAN_GET_DESCRIPTOR structure is used as a parameter to DeviceIoControl, when the specified I/O control code is IOCTL_GET_USB_DESCRIPTOR. |
| [USBSCAN_TIMEOUT structure](..\usbscan\ns-usbscan--usbscan-timeout.md) | The USBSCAN_TIMEOUT structure stores time-out values for USB bulk IN and bulk OUT operations, and interrupts. |
| [CHANNEL_INFO structure](..\usbscan\ns-usbscan--channel-info.md) | The CHANNEL_INFO structure is used as a parameter to DeviceIoControl, when the specified I/O control code is IOCTL_GET_CHANNEL_ALIGN_RQST. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [RAW_PIPE_TYPE enumeration](..\usbscan\ne-usbscan--raw-pipe-type.md) | The RAW_PIPE_TYPE data type is used to specify the type of a USB pipe. |
| [PIPE_TYPE enumeration](..\usbscan\ne-usbscan-pipe-type.md) | The PIPE_TYPE data type is used as input to the DeviceIoControl function, if the I/O control code is IOCTL_CANCEL_IO or IOCTL_RESET_PIPE. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [tagDEVICEDIALOGDATA2 structure](..\wiadevd\ns-wiadevd-tagdevicedialogdata2.md) | The DEVICEDIALOGDATA2 structure contains all the data needed to implement a custom device dialog. |
| [tagDEVICEDIALOGDATA structure](..\wiadevd\ns-wiadevd-tagdevicedialogdata.md) | The DEVICEDIALOGDATA structure contains all the data needed to implement a custom device dialog. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [wiasSetPropChanged function](..\wiamdef\nf-wiamdef-wiassetpropchanged.md) | The wiasSetPropChanged function modifies a property context to indicate that a property is being changed. |
| [wiasGetItemType function](..\wiamdef\nf-wiamdef-wiasgetitemtype.md) | The wiasGetItemType function indicates the item type. |
| [CWiaLogProc::CWiaLogProc method](..\wiamdef\nf-wiamdef-cwialogproc-cwialogproc.md) | The CWiaLogProc constructor is called when the function or method being logged is entered. |
| [wiasCreatePropContext function](..\wiamdef\nf-wiamdef-wiascreatepropcontext.md) | The wiasCreatePropContext function allocates a property context to indicate which of an item's properties are being changed by the application. |
| [wiasReadPropGuid function](..\wiamdef\nf-wiamdef-wiasreadpropguid.md) | The wiasReadPropGuid function retrieves a GUID property value from a WIA item. |
| [wiasWritePageBufToFile function](..\wiamdef\nf-wiamdef-wiaswritepagebuftofile.md) | The wiasWritePageBufToFile function writes the contents of a temporary page buffer to an image file. |
| [wiasWriteBufToFile function](..\wiamdef\nf-wiamdef-wiaswritebuftofile.md) | The wiasWriteBufToFile function writes from a specified buffer to an image file. |
| [wiasGetDrvItem function](..\wiamdef\nf-wiamdef-wiasgetdrvitem.md) | The wiasGetDrvItem function retrieves a driver item. |
| [wiasUpdateValidFormat function](..\wiamdef\nf-wiamdef-wiasupdatevalidformat.md) | The wiasUpdateValidFormat function updates the valid format of the property context for the current minidriver. |
| [wiasParseEndorserString function](..\wiamdef\nf-wiamdef-wiasparseendorserstring.md) | The wiasParseEndorserString function parses an endorser string, replacing WIA service-defined and vendor-defined tokens in the string with values associated with those tokens. |
| [wiasFreePropContext function](..\wiamdef\nf-wiamdef-wiasfreepropcontext.md) | The wiasFreePropContext function releases the memory occupied by a WIA_PROPERTY_CONTEXT structure. |
| [wiasReadPropFloat function](..\wiamdef\nf-wiamdef-wiasreadpropfloat.md) | The wiasReadPropFloat function retrieves a floating-point property value from a WIA item. |
| [wiasGetContextFromName function](..\wiamdef\nf-wiamdef-wiasgetcontextfromname.md) | The wiasGetContextFromName function retrieves the item context for an item name. |
| [wiasWritePropBin function](..\wiamdef\nf-wiamdef-wiaswritepropbin.md) | The wiasWritePropBin function writes a single binary-data property value to a WIA item. |
| [wiasDebugError function](..\wiamdef\nf-wiamdef-wiasdebugerror.md) | This function prints a debug error string in the Device Manager debug console. The output color is always red. |
| [wiasGetChangedValueLong function](..\wiamdef\nf-wiamdef-wiasgetchangedvaluelong.md) | The wiasGetChangedValueLong function determines whether a property with a long integer value has been changed by an application. |
| [wiasWritePropLong function](..\wiamdef\nf-wiamdef-wiaswriteproplong.md) | The wiasWritePropLong function writes a single long integer property value to a WIA item. |
| [CWiaLogProcEx::~CWiaLogProcEx method](..\wiamdef\nf-wiamdef-cwialogprocex-~cwialogprocex.md) | The~CWiaLogProcEx destructor is called when the function or method being logged is exited. |
| [wiasSetPropertyAttributes function](..\wiamdef\nf-wiamdef-wiassetpropertyattributes.md) | The wiasSetPropertyAttributes function sets the access flags and valid values for a set of properties. |
| [wiasPrintDebugHResult function](..\wiamdef\nf-wiamdef-wiasprintdebughresult.md) | The wiasPrintDebugHResult function is obsolete for Windows XP and later, and is no longer supported. Use the WIAS_LHRESULT macro instead.This function prints an HRESULT string on the Device Manager debug console. |
| [wiasSetItemPropAttribs function](..\wiamdef\nf-wiamdef-wiassetitempropattribs.md) | The wiasSetItemPropAttribs function sets the access flags and valid values for an item's set of properties. |
| [CWiaLogProc::~CWiaLogProc method](..\wiamdef\nf-wiamdef-cwialogproc-~cwialogproc.md) | The ~CWiaLogProc destructor is called when the function or method being logged is exited. |
| [wiasQueueEvent function](..\wiamdef\nf-wiamdef-wiasqueueevent.md) | The wiasQueueEvent function informs the service that the device generated an event. |
| [wiasCreateLogInstance function](..\wiamdef\nf-wiamdef-wiascreateloginstance.md) | The wiasCreateLogInstance function creates an instance of a logging object. |
| [wiasSetValidListGuid function](..\wiamdef\nf-wiamdef-wiassetvalidlistguid.md) | The wiasSetValidListGuid function sets valid values for a WIA_PROP_LIST property of type VT_CLSID. |
| [wiasDownSampleBuffer function](..\wiamdef\nf-wiamdef-wiasdownsamplebuffer.md) | The wiasDownSampleBuffer function takes in a buffer of DWORD-aligned pixel data and downsamples it (produces image data of lower resolution) to the specified size and resolution. |
| [wiasGetImageInformation function](..\wiamdef\nf-wiamdef-wiasgetimageinformation.md) | The wiasGetImageInformation function retrieves transfer context information from an item. |
| [wiasSendEndOfPage function](..\wiamdef\nf-wiamdef-wiassendendofpage.md) | The wiasSendEndOfPage function calls the client callback routine during a data transfer, sending the current total page count. |
| [wiasWritePropStr function](..\wiamdef\nf-wiamdef-wiaswritepropstr.md) | The wiasWritePropStr function writes a single string property value to a WIA item. |
| [wiasGetChangedValueStr function](..\wiamdef\nf-wiamdef-wiasgetchangedvaluestr.md) | The wiasGetChangedValueStr function determines whether a property with a string value has been changed by an application. |
| [wiasWritePageBufToStream function](..\wiamdef\nf-wiamdef-wiaswritepagebuftostream.md) | The wiasWritePageBufToStream function writes the contents of a temporary page buffer to the IStream interface provided by the application. |
| [wiasCreateChildAppItem function](..\wiamdef\nf-wiamdef-wiascreatechildappitem.md) | The wiasCreateChildAppItem function creates a new application item and inserts it as a child of the specified (parent) item. Note that this item will not have any properties in its property sets until the driver or application actually fills them in. |
| [wiasValidateItemProperties function](..\wiamdef\nf-wiamdef-wiasvalidateitemproperties.md) | The wiasValidateItemProperties function validates a list of simple item properties against their current valid values. |
| [wiasSetValidFlag function](..\wiamdef\nf-wiamdef-wiassetvalidflag.md) | The wiasSetValidFlag function sets the valid values for a WIA_PROP_FLAG property. |
| [wiasWriteMultiple function](..\wiamdef\nf-wiamdef-wiaswritemultiple.md) | The wiasWriteMultiple function writes multiple property values to a WIA item. |
| [wiasSetValidListLong function](..\wiamdef\nf-wiamdef-wiassetvalidlistlong.md) | The wiasSetValidListLong function sets the valid values for a WIA_PROP_LIST property of type VT_I4. |
| [wiasGetChangedValueFloat function](..\wiamdef\nf-wiamdef-wiasgetchangedvaluefloat.md) | The wiasGetChangedValueFloat function determines whether a property with a floating-point value has been changed by an application. |
| [wiasWritePropFloat function](..\wiamdef\nf-wiamdef-wiaswritepropfloat.md) | The wiasWritePropFloat function writes a single floating-point property value to a WIA item. |
| [wiasSetValidRangeLong function](..\wiamdef\nf-wiamdef-wiassetvalidrangelong.md) | The wiasSetValidRangeLong function specifies the range of valid values for a WIA_PROP_RANGE property of type VT_I4. |
| [wiasSetItemPropNames function](..\wiamdef\nf-wiamdef-wiassetitempropnames.md) | The wiasSetItemPropNames function writes property names to item properties. |
| [wiasSetValidListStr function](..\wiamdef\nf-wiamdef-wiassetvalidliststr.md) | The wiasSetValidListStr function sets the valid values for a WIA_PROP_LIST property of type VT_BSTR. |
| [wiasCreateDrvItem function](..\wiamdef\nf-wiamdef-wiascreatedrvitem.md) | The wiasCreateDrvItem function creates an IWiaDrvItem Interface object. |
| [wiasSetValidRangeFloat function](..\wiamdef\nf-wiamdef-wiassetvalidrangefloat.md) | The wiasSetValidRangeFloat function specifies the range of valid values for a WIA_PROP_RANGE property of type VT_R4. |
| [wiasGetChildrenContexts function](..\wiamdef\nf-wiamdef-wiasgetchildrencontexts.md) | The wiasGetChildrenContexts function retrieves an array of item contexts belonging to the current item's children. |
| [wiasUpdateScanRect function](..\wiamdef\nf-wiamdef-wiasupdatescanrect.md) | The wiasUpdateScanRect function updates the scanning area sizes of the scanning device. |
| [CWiaLogProcEx::CWiaLogProcEx method](..\wiamdef\nf-wiamdef-cwialogprocex-cwialogprocex.md) | The CWiaLogProcEx constructor is called when the function or method being logged is entered. |
| [wiasSetValidListFloat function](..\wiamdef\nf-wiamdef-wiassetvalidlistfloat.md) | The wiasSetValidListFloat function sets valid values for a WIA_PROP_LIST property of type VT_R4. |
| [wiasReadPropStr function](..\wiamdef\nf-wiamdef-wiasreadpropstr.md) | The wiasReadPropStr function retrieves a string property value from a WIA item. |
| [wiasFormatArgs function](..\wiamdef\nf-wiamdef-wiasformatargs.md) | The wiasFormatArgs function formats an argument list into a packaged string for logging. |
| [wiasIsPropChanged function](..\wiamdef\nf-wiamdef-wiasispropchanged.md) | The wiasIsPropChanged function tests whether a specified property has been changed by an application. |
| [wiasReadPropLong function](..\wiamdef\nf-wiamdef-wiasreadproplong.md) | The wiasReadPropLong function retrieves a long integer property value from a WIA item. |
| [wiasReadPropBin function](..\wiamdef\nf-wiamdef-wiasreadpropbin.md) | The wiasReadPropBin function retrieves a binary-data property value from a WIA item. |
| [wiasGetChangedValueGuid function](..\wiamdef\nf-wiamdef-wiasgetchangedvalueguid.md) | The wiasGetChangedValueGuid function determines whether a property with a GUID value has been changed by an application. |
| [wiasGetRootItem function](..\wiamdef\nf-wiamdef-wiasgetrootitem.md) | The wiasGetRootItem function retrieves the root item context of a specified WIA item. |
| [wiasReadMultiple function](..\wiamdef\nf-wiamdef-wiasreadmultiple.md) | The wiasReadMultiple function retrieves multiple property values from a WIA item. |
| [wiasGetPropertyAttributes function](..\wiamdef\nf-wiamdef-wiasgetpropertyattributes.md) | The wiasGetPropertyAttributes function retrieves the access flags and valid values for a set of properties. |
| [wiasDebugTrace function](..\wiamdef\nf-wiamdef-wiasdebugtrace.md) | This function prints a debug trace string in the Device Manager debug console. |
| [wiasWritePropGuid function](..\wiamdef\nf-wiamdef-wiaswritepropguid.md) | The wiasWritePropGuid function writes a single GUID property value to a WIA item. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [MicroEntry function](..\wiamicro\nf-wiamicro-microentry.md) | The MicroEntry function responds to commands sent by the WIA Flatbed driver. |
| [SetPixelWindow function](..\wiamicro\nf-wiamicro-setpixelwindow.md) | The SetPixelWindow function sets the image area to be scanned. |
| [Scan function](..\wiamicro\nf-wiamicro-scan.md) | The Scan function reads data from the device and returns the data to the WIA Flatbed driver. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [SCANWINDOW structure](..\wiamicro\ns-wiamicro--scanwindow.md) | The SCANWINDOW structure is used by the WIA Flatbed driver to tell the microdriver what image area to scan. |
| [SCANINFO structure](..\wiamicro\ns-wiamicro--scaninfo.md) | The SCANINFO structure is used to store and communicate information about a scan acquisition. |
| [RANGEVALUE structure](..\wiamicro\ns-wiamicro--rangevalue.md) | The RANGEVALUE structure is used by a microdriver to communicate to the WIA Flatbed driver the legal values for a microdriver function parameter. |
| [VAL structure](..\wiamicro\ns-wiamicro-val.md) | The VAL structure is used by the microdriver and WIA Flatbed driver to pass information between each other. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [IWiaMiniDrv::drvGetWiaFormatInfo method](..\wiamindr_lh\nf-wiamindr-lh-iwiaminidrv-drvgetwiaformatinfo.md) | The IWiaMiniDrv |
| [IWiaMiniDrvTransferCallback::GetNextStream method](..\wiamindr_lh\nf-wiamindr-lh-iwiaminidrvtransfercallback-getnextstream.md) | Called by the WIA mini-driver to obtain a stream for the current data transfer (download or upload). |
| [IWiaDrvItem::GetDeviceSpecContext method](..\wiamindr_lh\nf-wiamindr-lh-iwiadrvitem-getdevicespeccontext.md) | The IWiaDrvItem |
| [IWiaDrvItem::GetItemName method](..\wiamindr_lh\nf-wiamindr-lh-iwiadrvitem-getitemname.md) | The IWiaDrvItem |
| [IWiaDrvItem::GetFullItemName method](..\wiamindr_lh\nf-wiamindr-lh-iwiadrvitem-getfullitemname.md) | The IWiaDrvItem |
| [IWiaMiniDrv::drvWriteItemProperties method](..\wiamindr_lh\nf-wiamindr-lh-iwiaminidrv-drvwriteitemproperties.md) | The IWiaMiniDrv |
| [IWiaDrvItem::GetFirstChildItem method](..\wiamindr_lh\nf-wiamindr-lh-iwiadrvitem-getfirstchilditem.md) | The IWiaDrvItem |
| [IWiaDrvItem::GetParentItem method](..\wiamindr_lh\nf-wiamindr-lh-iwiadrvitem-getparentitem.md) | The IWiaDrvItem |
| [IWiaMiniDrv::drvReadItemProperties method](..\wiamindr_lh\nf-wiamindr-lh-iwiaminidrv-drvreaditemproperties.md) | The IWiaMiniDrv |
| [IWiaMiniDrv::drvDeleteItem method](..\wiamindr_lh\nf-wiamindr-lh-iwiaminidrv-drvdeleteitem.md) | The IWiaMiniDrv |
| [IWiaMiniDrv::drvDeviceCommand method](..\wiamindr_lh\nf-wiamindr-lh-iwiaminidrv-drvdevicecommand.md) | The IWiaMiniDrv |
| [IWiaMiniDrv::drvGetDeviceErrorStr method](..\wiamindr_lh\nf-wiamindr-lh-iwiaminidrv-drvgetdeviceerrorstr.md) | The IWiaMiniDrv |
| [IWiaMiniDrvCallBack::MiniDrvCallback method](..\wiamindr_lh\nf-wiamindr-lh-iwiaminidrvcallback-minidrvcallback.md) | The IWiaMiniDrvCallBack |
| [IWiaDrvItem::DumpItemData method](..\wiamindr_lh\nf-wiamindr-lh-iwiadrvitem-dumpitemdata.md) | The IWiaDrvItem |
| [IWiaMiniDrv::drvNotifyPnpEvent method](..\wiamindr_lh\nf-wiamindr-lh-iwiaminidrv-drvnotifypnpevent.md) | The IWiaMiniDrv |
| [IWiaMiniDrv::drvAnalyzeItem method](..\wiamindr_lh\nf-wiamindr-lh-iwiaminidrv-drvanalyzeitem.md) | The IWiaMiniDrv |
| [IWiaMiniDrv::drvUnLockWiaDevice method](..\wiamindr_lh\nf-wiamindr-lh-iwiaminidrv-drvunlockwiadevice.md) | The IWiaMiniDrv |
| [IWiaDrvItem::GetNextSiblingItem method](..\wiamindr_lh\nf-wiamindr-lh-iwiadrvitem-getnextsiblingitem.md) | The IWiaDrvItem |
| [IWiaMiniDrv::drvAcquireItemData method](..\wiamindr_lh\nf-wiamindr-lh-iwiaminidrv-drvacquireitemdata.md) | The IWiaMiniDrv |
| [IWiaDrvItem::FindChildItemByName method](..\wiamindr_lh\nf-wiamindr-lh-iwiadrvitem-findchilditembyname.md) | The IWiaDrvItem |
| [IWiaMiniDrvTransferCallback::SendMessage method](..\wiamindr_lh\nf-wiamindr-lh-iwiaminidrvtransfercallback-sendmessage.md) | Periodically called by the WIA mini-driver during a data transfer, to update the WIA application client about the progress and status of the transfer. |
| [IWiaDrvItem::UnlinkItemTree method](..\wiamindr_lh\nf-wiamindr-lh-iwiadrvitem-unlinkitemtree.md) | The IWiaDrvItem |
| [IWiaDrvItem::RemoveItemFromFolder method](..\wiamindr_lh\nf-wiamindr-lh-iwiadrvitem-removeitemfromfolder.md) | The IWiaDrvItem |
| [IWiaMiniDrv::drvInitItemProperties method](..\wiamindr_lh\nf-wiamindr-lh-iwiaminidrv-drvinititemproperties.md) | The IWiaMiniDrv |
| [IWiaDrvItem::AddItemToFolder method](..\wiamindr_lh\nf-wiamindr-lh-iwiadrvitem-additemtofolder.md) | The IWiaDrvItem |
| [IWiaMiniDrv::drvGetCapabilities method](..\wiamindr_lh\nf-wiamindr-lh-iwiaminidrv-drvgetcapabilities.md) | The IWiaMiniDrv |
| [IWiaMiniDrv::drvUnInitializeWia method](..\wiamindr_lh\nf-wiamindr-lh-iwiaminidrv-drvuninitializewia.md) | The IWiaMiniDrv |
| [IWiaMiniDrv::drvInitializeWia method](..\wiamindr_lh\nf-wiamindr-lh-iwiaminidrv-drvinitializewia.md) | The IWiaMiniDrv |
| [IWiaDrvItem::FindItemByName method](..\wiamindr_lh\nf-wiamindr-lh-iwiadrvitem-finditembyname.md) | The IWiaDrvItem |
| [IWiaDrvItem::GetItemFlags method](..\wiamindr_lh\nf-wiamindr-lh-iwiadrvitem-getitemflags.md) | The IWiaDrvItem |
| [IWiaMiniDrv::drvFreeDrvItemContext method](..\wiamindr_lh\nf-wiamindr-lh-iwiaminidrv-drvfreedrvitemcontext.md) | The IWiaMiniDrv |
| [IWiaMiniDrv::drvLockWiaDevice method](..\wiamindr_lh\nf-wiamindr-lh-iwiaminidrv-drvlockwiadevice.md) | The IWiaMiniDrv |
| [IWiaMiniDrv::drvValidateItemProperties method](..\wiamindr_lh\nf-wiamindr-lh-iwiaminidrv-drvvalidateitemproperties.md) | The IWiaMiniDrv |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WIA_PROPERTY_INFO structure](..\wiamindr_lh\ns-wiamindr-lh--wia-property-info.md) | The WIA_PROPERTY_INFO structure is used to store default access and valid value information for an item property of arbitrary type. |
| [WIAS_DOWN_SAMPLE_INFO structure](..\wiamindr_lh\ns-wiamindr-lh--wias-down-sample-info.md) | The WIAS_DOWN_SAMPLE_INFO structure stores information used by the downsampling helper function, wiasDownSampleBuffer. |
| [WIAS_ENDORSER_INFO structure](..\wiamindr_lh\ns-wiamindr-lh--wias-endorser-info.md) | The WIAS_ENDORSER_INFO structure holds custom endorser token/value pairs. |
| [MINIDRV_TRANSFER_CONTEXT structure](..\wiamindr_lh\ns-wiamindr-lh--minidrv-transfer-context.md) | The MINIDRV_TRANSFER_CONTEXT structure is used to store image and other information needed for a memory-callback data transfer or a file data transfer. |
| [WIA_PROPERTY_CONTEXT structure](..\wiamindr_lh\ns-wiamindr-lh--wia-property-context.md) | The WIA_PROPERTY_CONTEXT structure stores property identifiers and their context. |
| [WIA_DEV_CAP_DRV structure](..\wiamindr_lh\ns-wiamindr-lh--wia-dev-cap-drv.md) | The WIA_DEV_CAP_DRV structure is used to enumerate device capabilities. A device capability is defined by an event or command that the device supports. |
| [WIAS_ENDORSER_VALUE structure](..\wiamindr_lh\ns-wiamindr-lh--wias-endorser-value.md) | The WIAS_ENDORSER_VALUE structure stores token/value pairs for endorser strings. |
| [WIAS_CHANGED_VALUE_INFO structure](..\wiamindr_lh\ns-wiamindr-lh--wias-changed-value-info.md) | The WIAS_CHANGED_VALUE_INFO structure is used to store the current and previous values of a property. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [TWAIN_CAPABILITY structure](..\wiatwcmp\ns-wiatwcmp--twain-capability.md) | The TWAIN_CAPABILITY structure holds information used when a TWAIN-compatible application communicates with a WIA driver. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [CWiauPropertyList::GetPropId method](..\wiautil\nf-wiautil-cwiaupropertylist-getpropid.md) | The CWiauPropertyList |
| [wiauSetImageItemSize function](..\wiautil\nf-wiautil-wiausetimageitemsize.md) | The wiauSetImageItemSize function calculates the size and width, in bytes, for an image, based on the current WIA_IPA_FORMAT setting (described in the Microsoft Windows SDK documentation), and writes the new values to the appropriate properties. |
| [wiauStrC2W function](..\wiautil\nf-wiautil-wiaustrc2w.md) | The wiauStrC2W function converts an ANSI character string to a Unicode string. |
| [wiauGetDrvItemContext function](..\wiautil\nf-wiautil-wiaugetdrvitemcontext.md) | The wiauGetDrvItemContext function gets the driver item context, and optionally, the driver item. |
| [wiauDbgError function](..\wiautil\nf-wiautil-wiaudbgerror.md) | The wiauDbgError function logs an error message. |
| [wiauDbgFlags function](..\wiautil\nf-wiautil-wiaudbgflags.md) | The wiauDbgFlags function determines whether a particular debugging flag is set. |
| [CWiauFormatConverter::~CWiauFormatConverter method](..\wiautil\nf-wiautil-cwiauformatconverter-~cwiauformatconverter.md) | The CWiauFormatConverter |
| [wiauDbgLegacyHresult2 function](..\wiautil\nf-wiautil-wiaudbglegacyhresult2.md) | The wiauDbgLegacyHresult2 function logs a default message containing an HRESULT. |
| [wiauDbgHelper function](..\wiautil\nf-wiautil-wiaudbghelper~r1.md) | The wiauDbgHelper function formats a message and writes it to a log file, or debugger, or both. |
| [wiauGetValidFormats function](..\wiautil\nf-wiautil-wiaugetvalidformats~r1.md) | The wiauGetValidFormats function calls the IWiaMiniDrv |
| [wiauPropsInPropSpec function](..\wiautil\nf-wiautil-wiaupropsinpropspec~r1.md) | The wiauPropsInPropSpec function determines whether any of a list of property specification IDs is contained within an array of such values. |
| [wiauDbgSetFlags function](..\wiautil\nf-wiautil-wiaudbgsetflags~r1.md) | The wiauDbgSetFlags function sets debugging flags. |
| [CWiauFormatConverter::ConvertToBmp method](..\wiautil\nf-wiautil-cwiauformatconverter-converttobmp.md) | The CWiauFormatConverter |
| [wiauGetResourceString function](..\wiautil\nf-wiautil-wiaugetresourcestring~r1.md) | The wiauGetResourceString function gets a resource string, storing it as a BSTR. |
| [wiauPropsInPropSpec function](..\wiautil\nf-wiautil-wiaupropsinpropspec.md) | The wiauPropsInPropSpec function determines whether any of a list of property specification IDs is contained within an array of such values. |
| [wiauPropInPropSpec function](..\wiautil\nf-wiautil-wiaupropinpropspec.md) | The wiauPropInPropSpec function determines whether a specified property specification ID is contained in an array of such values. The function optionally gets the index at which the property specification ID was found. |
| [CWiauPropertyList::DefineProperty method](..\wiautil\nf-wiautil-cwiaupropertylist-defineproperty.md) | The CWiauPropertyList |
| [wiauDbgErrorHr function](..\wiautil\nf-wiautil-wiaudbgerrorhr.md) | The wiauDbgErrorHr function logs a message containing an HRESULT and its error message string. |
| [CWiauPropertyList::SendToWia method](..\wiautil\nf-wiautil-cwiaupropertylist-sendtowia.md) | The CWiauPropertyList |
| [CWiauPropertyList::Init method](..\wiautil\nf-wiautil-cwiaupropertylist-init.md) | The CWiauPropertyList |
| [wiauDbgDump function](..\wiautil\nf-wiautil-wiaudbgdump.md) | The wiauDbgDump function logs a message containing one or more data values. |
| [wiauDbgInit function](..\wiautil\nf-wiautil-wiaudbginit.md) | The wiauDbgInit function initializes WIA debugging. |
| [CWiauDbgFn::CWiauDbgFn method](..\wiautil\nf-wiautil-cwiaudbgfn-cwiaudbgfn.md) | The CWiauDbgFn |
| [wiauDbgInit function](..\wiautil\nf-wiautil-wiaudbginit~r1.md) | The wiauDbgInit function initializes WIA debugging. |
| [wiauStrW2W function](..\wiautil\nf-wiautil-wiaustrw2w~r1.md) | The wiauStrW2W function copies a Unicode string to another Unicode string. |
| [wiauDbgSetFlags function](..\wiautil\nf-wiautil-wiaudbgsetflags.md) | The wiauDbgSetFlags function sets debugging flags. |
| [wiauStrC2C function](..\wiautil\nf-wiautil-wiaustrc2c~r1.md) | The wiauStrC2C function copies an ANSI character string to another ANSI character string. |
| [wiauDbgHelper2 function](..\wiautil\nf-wiautil-wiaudbghelper2.md) | The wiauDbgHelper2 function writes a message to a log file, or debugger, or both. |
| [wiauDbgLegacyWarning function](..\wiautil\nf-wiautil-wiaudbglegacywarning.md) | The wiauDbgLegacyWarning function logs a warning message. |
| [CWiauFormatConverter::Init method](..\wiautil\nf-wiautil-cwiauformatconverter-init.md) | The CWiauFormatConverter |
| [wiauStrW2C function](..\wiautil\nf-wiautil-wiaustrw2c.md) | The wiauStrW2C function converts a Unicode string to an ANSI character string. |
| [wiauDbgHelper function](..\wiautil\nf-wiautil-wiaudbghelper.md) | The wiauDbgHelper function formats a message and writes it to a log file, or debugger, or both. |
| [CWiauPropertyList::SetAccessSubType method](..\wiautil\nf-wiautil-cwiaupropertylist-setaccesssubtype~r1.md) | The CWiauPropertyList |
| [wiauSetImageItemSize function](..\wiautil\nf-wiautil-wiausetimageitemsize~r1.md) | The wiauSetImageItemSize function calculates the size and width, in bytes, for an image, based on the current WIA_IPA_FORMAT setting (described in the Microsoft Windows SDK documentation), and writes the new values to the appropriate properties. |
| [CWiauPropertyList::SetAccessSubType method](..\wiautil\nf-wiautil-cwiaupropertylist-setaccesssubtype.md) | The CWiauPropertyList |
| [wiauStrC2W function](..\wiautil\nf-wiautil-wiaustrc2w~r1.md) | The wiauStrC2W function converts an ANSI character string to a Unicode string. |
| [wiauDbgTrace function](..\wiautil\nf-wiautil-wiaudbgtrace.md) | The wiauDbgTrace function logs a trace message. |
| [wiauGetDrvItemContext function](..\wiautil\nf-wiautil-wiaugetdrvitemcontext~r1.md) | The wiauGetDrvItemContext function gets the driver item context, and optionally, the driver item. |
| [CWiauPropertyList::~CWiauPropertyList method](..\wiautil\nf-wiautil-cwiaupropertylist-~cwiaupropertylist.md) | The CWiauPropertyList |
| [wiauDbgLegacyTrace function](..\wiautil\nf-wiautil-wiaudbglegacytrace.md) | The wiauDbgLegacyTrace function logs a trace message. |
| [wiauDbgLegacyTrace2 function](..\wiautil\nf-wiautil-wiaudbglegacytrace2.md) | The wiauDbgLegacyTrace2 function logs a trace message. |
| [CWiauPropertyList::LookupPropId method](..\wiautil\nf-wiautil-cwiaupropertylist-lookuppropid.md) | The CWiauPropertyList |
| [wiauGetResourceString function](..\wiautil\nf-wiautil-wiaugetresourcestring.md) | The wiauGetResourceString function gets a resource string, storing it as a BSTR. |
| [wiauDbgLegacyError2 function](..\wiautil\nf-wiautil-wiaudbglegacyerror2.md) | The wiauDbgLegacyError2 function logs an error message. |
| [wiauDbgWarning function](..\wiautil\nf-wiautil-wiaudbgwarning.md) | The wiauDbgWarning function logs a warning message. |
| [CWiauPropertyList::CWiauPropertyList method](..\wiautil\nf-wiautil-cwiaupropertylist-cwiaupropertylist.md) | The CWiauPropertyList |
| [wiauStrW2W function](..\wiautil\nf-wiautil-wiaustrw2w.md) | The wiauStrW2W function copies a Unicode string to another Unicode string. |
| [CWiauFormatConverter::IsFormatSupported method](..\wiautil\nf-wiautil-cwiauformatconverter-isformatsupported.md) | The CWiauFormatConverter |
| [wiauDbgLegacyError function](..\wiautil\nf-wiautil-wiaudbglegacyerror.md) | The wiauDbgLegacyError function logs an error message. |
| [wiauPropInPropSpec function](..\wiautil\nf-wiautil-wiaupropinpropspec~r1.md) | The wiauPropInPropSpec function determines whether a specified property specification ID is contained in an array of such values. The function optionally gets the index at which the property specification ID was found. |
| [CWiauFormatConverter::CWiauFormatConverter method](..\wiautil\nf-wiautil-cwiauformatconverter-cwiauformatconverter.md) | The CWiauFormatConverter |
| [wiauGetValidFormats function](..\wiautil\nf-wiautil-wiaugetvalidformats.md) | The wiauGetValidFormats function calls the IWiaMiniDrv |
| [wiauStrC2C function](..\wiautil\nf-wiautil-wiaustrc2c.md) | The wiauStrC2C function copies an ANSI character string to another ANSI character string. |
| [wiauStrW2C function](..\wiautil\nf-wiautil-wiaustrw2c~r1.md) | The wiauStrW2C function converts a Unicode string to an ANSI character string. |
| [CWiauDbgFn::~CWiauDbgFn method](..\wiautil\nf-wiautil-cwiaudbgfn-~cwiaudbgfn.md) | The CWiauDbgFn |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [SKIP_AMOUNT enumeration](..\wiautil\ne-wiautil-skip-amount.md) | The SKIP_AMOUNT enumeration is used to indicate whether the file and informational headers of an image should be skipped over. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [BMP_IMAGE_INFO structure](..\wiautil\ns-wiautil--bmp-image-info.md) | The BMP_IMAGE_INFO structure contains information about a BMP image. |


This technology is in the following headers:


| Header        | 

| [ptpusd](..\ptpusd\~PORTAL~ptpusd.md) | 

| [scsiscan](..\scsiscan\~PORTAL~scsiscan.md) | 

| [sti](..\sti\~PORTAL~sti.md) | 

| [stiusd](..\stiusd\~PORTAL~stiusd.md) | 

| [usbscan](..\usbscan\~PORTAL~usbscan.md) | 

| [wiadef](..\wiadef\~PORTAL~wiadef.md) | 

| [wiadevd](..\wiadevd\~PORTAL~wiadevd.md) | 

| [wiamdef](..\wiamdef\~PORTAL~wiamdef.md) | 

| [wiamicro](..\wiamicro\~PORTAL~wiamicro.md) | 

| [wiamindr_lh](..\wiamindr_lh\~PORTAL~wiamindr_lh.md) | 

| [wiatwcmp](..\wiatwcmp\~PORTAL~wiatwcmp.md) | 

| [wiautil](..\wiautil\~PORTAL~wiautil.md) | 
