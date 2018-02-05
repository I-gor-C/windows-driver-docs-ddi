---
UID : NE:pointofservicedriverinterface._PosDeviceControlType
title : "_PosDeviceControlType"
author : windows-driver-content
description : This enumeration defines values for the IOCTLs of the scanner driver and magnetic stripe reader (MSR) driver.
old-location : pos\posdevicecontroltype.htm
old-project : pos
ms.assetid : 9f5f3baa-49a0-4711-88c0-b9ff8d87ae1d
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : pointofservicedriverinterface/UpdateStatistics, _PosDeviceControlType, UpdateStatistics, pointofservicedriverinterface/BarcodeScannerInjectEvent, MsrRetrieveDeviceAuthentication, RetrieveStatistics, pointofservicedriverinterface/MsrAuthenticateDevice, pointofservicedriverinterface/ReleaseDevice, pointofservicedriverinterface/MsrUpdateKey, pointofservicedriverinterface/_MaxDeviceControlType, pointofservicedriverinterface/SetProperty, pointofservicedriverinterface/RetrieveStatistics, pointofservicedriverinterface/CheckHealth, MsrAuthenticateDevice, pointofservicedriverinterface/ResetStatistics, RetainDevice, pointofservicedriverinterface/MsrDeAuthenticateDevice, ResetStatistics, ReleaseDevice, CheckHealth, pointofservicedriverinterface/GetProperty, GetDeviceBasics, MsrDeAuthenticateDevice, _MaxDeviceControlType, ClaimDevice, MsrUpdateKey, pointofservicedriverinterface/MsrRetrieveDeviceAuthentication, pos.posdevicecontroltype, GetProperty, pointofservicedriverinterface/Invalid, pointofservicedriverinterface/RetainDevice, PosDeviceControlType enumeration, pointofservicedriverinterface/PosDeviceControlType, pointofservicedriverinterface/GetDeviceBasics, SetProperty, pointofservicedriverinterface/ClaimDevice, PosDeviceControlType, BarcodeScannerInjectEvent, Invalid
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : pointofservicedriverinterface.h
req.include-header : Pointofservicedriverinterface.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : Called at PASSIVE_LEVEL.
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : PosDeviceControlType
---

# _PosDeviceControlType Enumeration
This enumeration defines values for the IOCTLs of the scanner driver and magnetic stripe reader (MSR) driver.

## Syntax
````
typedef enum _PosDeviceControlType { 
  Invalid                          = 0,
  GetProperty                      = 1,
  SetProperty                      = 2,
  ClaimDevice                      = 3,
  ReleaseDevice                    = 4,
  RetainDevice                     = 5,
  RetrieveStatistics               = 6,
  ResetStatistics                  = 7,
  UpdateStatistics                 = 8,
  CheckHealth                      = 9,
  GetDeviceBasics                  = 10,
  BarcodeScannerInjectEvent        = 11,
  MsrRetrieveDeviceAuthentication  = 12,
  MsrAuthenticateDevice            = 13,
  MsrDeAuthenticateDevice          = 14,
  MsrUpdateKey                     = 15,
  _MaxDeviceControlType            = 16
} PosDeviceControlType;
````

## Constants

<table>

<tr>
<td>_MaxDeviceControlType</td>
<td></td>
</tr>

<tr>
<td>_MinDeviceControlType</td>
<td></td>
</tr>

<tr>
<td>BarcodeScannerGetSymbologyAttributes</td>
<td></td>
</tr>

<tr>
<td>BarcodeScannerInjectEvent</td>
<td>Unused.</td>
</tr>

<tr>
<td>BarcodeScannerSetSymbologyAttributes</td>
<td></td>
</tr>

<tr>
<td>CashDrawerCancelWait</td>
<td></td>
</tr>

<tr>
<td>CashDrawerCreateDrawerCloseAlarm</td>
<td></td>
</tr>

<tr>
<td>CashDrawerOpenDrawer</td>
<td></td>
</tr>

<tr>
<td>CheckHealth</td>
<td>Represents <a href="..\pointofservicedriverinterface\ni-pointofservicedriverinterface-ioctl_point_of_service_check_health.md">IOCTL_POINT_OF_SERVICE_CHECK_HEALTH</a>.</td>
</tr>

<tr>
<td>ClaimDevice</td>
<td>Represents <a href="..\pointofservicedriverinterface\ni-pointofservicedriverinterface-ioctl_point_of_service_claim_device.md">IOCTL_POINT_OF_SERVICE_CLAIM_DEVICE</a>.</td>
</tr>

<tr>
<td>ConnectRemotePosDevice</td>
<td></td>
</tr>

<tr>
<td>GetDeviceBasics</td>
<td>Represents <a href="..\pointofservicedriverinterface\ni-pointofservicedriverinterface-ioctl_point_of_service_get_device_basics.md">IOCTL_POINT_OF_SERVICE_GET_DEVICE_BASICS</a>.</td>
</tr>

<tr>
<td>GetProperty</td>
<td>Represents <a href="..\pointofservicedriverinterface\ni-pointofservicedriverinterface-ioctl_point_of_service_get_property.md">IOCTL_POINT_OF_SERVICE_GET_PROPERTY</a>.</td>
</tr>

<tr>
<td>Invalid</td>
<td>The event code is not valid.</td>
</tr>

<tr>
<td>LineDisplayClearDescriptors</td>
<td></td>
</tr>

<tr>
<td>LineDisplayCreateWindow</td>
<td></td>
</tr>

<tr>
<td>LineDisplayDefineGlyph</td>
<td></td>
</tr>

<tr>
<td>LineDisplayDestroyWindow</td>
<td></td>
</tr>

<tr>
<td>LineDisplayReadCharacterAtCursor</td>
<td></td>
</tr>

<tr>
<td>LineDisplayRefreshWindow</td>
<td></td>
</tr>

<tr>
<td>LineDisplaySetBitmap</td>
<td></td>
</tr>

<tr>
<td>LineDisplaySetDescriptor</td>
<td></td>
</tr>

<tr>
<td>LineDisplayWindowClearText</td>
<td></td>
</tr>

<tr>
<td>LineDisplayWindowDisplayBitmap</td>
<td></td>
</tr>

<tr>
<td>LineDisplayWindowDisplayText</td>
<td></td>
</tr>

<tr>
<td>LineDisplayWindowDisplayTextAt</td>
<td></td>
</tr>

<tr>
<td>LineDisplayWindowScrollText</td>
<td></td>
</tr>

<tr>
<td>MsrAuthenticateDevice</td>
<td>Represents <a href="..\pointofservicedriverinterface\ni-pointofservicedriverinterface-ioctl_point_of_service_msr_authenticate_device.md">IOCTL_POINT_OF_SERVICE_MSR_AUTHENTICATE_DEVICE</a>.</td>
</tr>

<tr>
<td>MsrDeAuthenticateDevice</td>
<td>Represents <a href="..\pointofservicedriverinterface\ni-pointofservicedriverinterface-ioctl_point_of_service_msr_deauthenticate_device.md">IOCTL_POINT_OF_SERVICE_MSR_DEAUTHENTICATE_DEVICE</a>.</td>
</tr>

<tr>
<td>MsrRetrieveDeviceAuthentication</td>
<td>Represents <a href="..\pointofservicedriverinterface\ni-pointofservicedriverinterface-ioctl_point_of_service_msr_retrieve_device_authentication.md">IOCTL_POINT_OF_SERVICE_MSR_RETRIEVE_DEVICE_AUTHENTICATION</a>.</td>
</tr>

<tr>
<td>MsrUpdateKey</td>
<td>Represents <a href="..\pointofservicedriverinterface\ni-pointofservicedriverinterface-ioctl_point_of_service_msr_update_key.md">IOCTL_POINT_OF_SERVICE_MSR_UPDATE_KEY</a>.</td>
</tr>

<tr>
<td>PrinterChangePrintSide</td>
<td></td>
</tr>

<tr>
<td>PrinterClearOutput</td>
<td></td>
</tr>

<tr>
<td>PrinterCutPaper</td>
<td></td>
</tr>

<tr>
<td>PrinterDrawRuledLine</td>
<td></td>
</tr>

<tr>
<td>PrinterMarkFeed</td>
<td></td>
</tr>

<tr>
<td>PrinterPageModePrint</td>
<td></td>
</tr>

<tr>
<td>PrinterPrintBarcode</td>
<td></td>
</tr>

<tr>
<td>PrinterPrintMemoryBitmapFill</td>
<td></td>
</tr>

<tr>
<td>PrinterPrintMemoryBitmapStart</td>
<td></td>
</tr>

<tr>
<td>PrinterPrintNormal</td>
<td></td>
</tr>

<tr>
<td>PrinterPrintSavedBitmap</td>
<td></td>
</tr>

<tr>
<td>PrinterRotatePrint</td>
<td></td>
</tr>

<tr>
<td>PrinterSetBitmapFill</td>
<td></td>
</tr>

<tr>
<td>PrinterSetBitmapStart</td>
<td></td>
</tr>

<tr>
<td>PrinterSlipCloseJaws</td>
<td></td>
</tr>

<tr>
<td>PrinterSlipOpenJaws</td>
<td></td>
</tr>

<tr>
<td>PrinterSlipWaitForPaperInserted</td>
<td></td>
</tr>

<tr>
<td>PrinterSlipWaitForPaperRemoved</td>
<td></td>
</tr>

<tr>
<td>PrinterTransactionPrint</td>
<td></td>
</tr>

<tr>
<td>PrinterValidateData</td>
<td></td>
</tr>

<tr>
<td>PrinterWaitForJobComplete</td>
<td></td>
</tr>

<tr>
<td>ReleaseDevice</td>
<td>Represents <a href="..\pointofservicedriverinterface\ni-pointofservicedriverinterface-ioctl_point_of_service_release_device.md">IOCTL_POINT_OF_SERVICE_RELEASE_DEVICE</a>.</td>
</tr>

<tr>
<td>ResetStatistics</td>
<td>Represents <a href="..\pointofservicedriverinterface\ni-pointofservicedriverinterface-ioctl_point_of_service_reset_statistics.md">IOCTL_POINT_OF_SERVICE_RESET_STATISTICS</a>.</td>
</tr>

<tr>
<td>RetainDevice</td>
<td>Represents <a href="..\pointofservicedriverinterface\ni-pointofservicedriverinterface-ioctl_point_of_service_retain_device.md">IOCTL_POINT_OF_SERVICE_RETAIN_DEVICE</a>.</td>
</tr>

<tr>
<td>RetrieveStatistics</td>
<td>Represents <a href="..\pointofservicedriverinterface\ni-pointofservicedriverinterface-ioctl_point_of_service_retrieve_statistics.md">IOCTL_POINT_OF_SERVICE_RETRIEVE_STATISTICS</a>.</td>
</tr>

<tr>
<td>SetProperty</td>
<td>Represents <a href="..\pointofservicedriverinterface\ni-pointofservicedriverinterface-ioctl_point_of_service_set_property.md">IOCTL_POINT_OF_SERVICE_SET_PROPERTY</a>.</td>
</tr>

<tr>
<td>StartBarcodeScannerSoftwareTrigger</td>
<td></td>
</tr>

<tr>
<td>StopBarcodeScannerSoftwareTrigger</td>
<td></td>
</tr>

<tr>
<td>UpdateStatistics</td>
<td>Represents <a href="..\pointofservicedriverinterface\ni-pointofservicedriverinterface-ioctl_point_of_service_update_statistics.md">IOCTL_POINT_OF_SERVICE_UPDATE_STATISTICS</a>.</td>
</tr>
</table>

## Remarks

This enumeration provides values for each IOCTL that you can send to the device driver. It is a convenient way to indicate which IOCTL to dispatch when calling functions like <b>SendDeviceCommand()</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | pointofservicedriverinterface.h (include Pointofservicedriverinterface.h) |