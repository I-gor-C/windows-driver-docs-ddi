---
UID : NE:ufxbase._USBFN_ACTION
title : "_USBFN_ACTION"
author : windows-driver-content
description : Defines special actions UFX should take when the client driver calls the UfxDevicePortDetectCompleteEx function.
old-location : buses\usbfn_action.htm
old-project : usbref
ms.assetid : 9E9AB3E0-EBDC-4EC3-BFBF-C78EE56BD699
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : buses.usbfn_action, UsbfnActionNone, USBFN_ACTION, UsbfnActionDetectProprietaryCharger, ufxbase/USBFN_ACTION, ufxbase/UsbfnActionNoCad, ufxbase/UsbfnActionDetectProprietaryCharger, *PUSBFN_ACTION, USBFN_ACTION enumeration [Buses], ufxbase/UsbfnActionNone, UsbfnActionNoCad, _USBFN_ACTION
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ufxbase.h
req.include-header : 
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
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PUSBFN_ACTION, USBFN_ACTION"
req.product : Windows 10 or later.
---

# _USBFN_ACTION Enumeration
Defines special actions UFX should take when the client driver calls the <a href="..\ufxclient\nf-ufxclient-ufxdeviceportdetectcompleteex.md">UfxDevicePortDetectCompleteEx</a> function.

## Syntax
````
typedef enum _USBFN_ACTION { 
  UsbfnActionNone                      = 0,
  UsbfnActionNoCad,
  UsbfnActionDetectProprietaryCharger
} USBFN_ACTION;
````

## Constants

<table>

<tr>
<td>UsbfnActionDetectProprietaryCharger</td>
<td>UFX should initiate proprietary charger detection by calling the client driver’s <a href="..\ufxclient\nc-ufxclient-evt_ufx_device_proprietary_charger_detect.md">EVT_UFX_DEVICE_DETECT_PROPRIETARY_CHARGER</a> callback function.</td>
</tr>

<tr>
<td>UsbfnActionNoCad</td>
<td>UFX should not notify the battery manager about the detected port type or the maximum current that can be drawn from the upstream port.</td>
</tr>

<tr>
<td>UsbfnActionNone</td>
<td>No special action should be taken.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ufxbase.h |