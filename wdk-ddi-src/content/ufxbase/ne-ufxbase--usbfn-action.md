---
UID: NE.ufxbase._USBFN_ACTION
title: USBFN_ACTION
author: windows-driver-content
description: Defines special actions UFX should take when the client driver calls the UfxDevicePortDetectCompleteEx function.
old-location: buses\usbfn_action.htm
old-project: usbref
ms.assetid: 9E9AB3E0-EBDC-4EC3-BFBF-C78EE56BD699
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: PUFS_UNIT_DESCRIPTOR, UFS_UNIT_DESCRIPTOR, *PUFS_UNIT_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ufxbase.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBFN_ACTION
req.alt-loc: ufxbase.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# USBFN_ACTION enumeration



## -description
<p>Defines special actions UFX should take when the client driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187963">UfxDevicePortDetectCompleteEx</a> function.</p>


## -syntax

````
typedef enum _USBFN_ACTION { 
  UsbfnActionNone                      = 0,
  UsbfnActionNoCad,
  UsbfnActionDetectProprietaryCharger
} USBFN_ACTION;
````


## -enum-fields
<dl>

### -field <a id="UsbfnActionNone"></a><a id="usbfnactionnone"></a><a id="USBFNACTIONNONE"></a><b>UsbfnActionNone</b>

<dd>
<p>No special action should be taken.</p>
</dd>

### -field <a id="UsbfnActionNoCad"></a><a id="usbfnactionnocad"></a><a id="USBFNACTIONNOCAD"></a><b>UsbfnActionNoCad</b>

<dd>
<p>UFX should not notify the battery manager about the detected port type or the maximum current that can be drawn from the upstream port.</p>
</dd>

### -field <a id="UsbfnActionDetectProprietaryCharger"></a><a id="usbfnactiondetectproprietarycharger"></a><a id="USBFNACTIONDETECTPROPRIETARYCHARGER"></a><b>UsbfnActionDetectProprietaryCharger</b>

<dd>
<p>UFX should initiate proprietary charger detection by calling the client driver’s <a href="https://msdn.microsoft.com/library/windows/hardware/mt187850">EVT_UFX_DEVICE_DETECT_PROPRIETARY_CHARGER</a> callback function.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ufxbase.h</dt>
</dl>
</td>
</tr>
</table>