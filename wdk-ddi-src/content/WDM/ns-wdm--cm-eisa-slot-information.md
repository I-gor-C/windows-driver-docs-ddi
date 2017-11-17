---
UID: NS.wdm._CM_EISA_SLOT_INFORMATION
title: CM_EISA_SLOT_INFORMATION
author: windows-driver-content
description: The CM_EISA_SLOT_INFORMATION structure defines EISA configuration header information returned by HalGetBusData for the input BusDataType = EisaConfiguration, or by HalGetBusDataByOffset for the inputs BusDataType = EisaConfiguration and Offset = 0, assuming the caller-allocated Buffer is of sufficient Length.
old-location: kernel\cm_eisa_slot_information.htm
ms.assetid: 443b6ed8-1d44-466f-93b0-bb8cd42aefaa
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CM_EISA_SLOT_INFORMATION
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
ms.keywords: CM_EISA_SLOT_INFORMATION, CM_EISA_SLOT_INFORMATION, *PCM_EISA_SLOT_INFORMATION
req.iface: 
req.product: Windows 10 or later.
---

# CM_EISA_SLOT_INFORMATION structure



## -description
<p>The <b>CM_EISA_SLOT_INFORMATION</b> structure defines EISA configuration header information returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff546599">HalGetBusData</a> for the input <i>BusDataType</i> =  <b>EisaConfiguration</b>, or by <a href="https://msdn.microsoft.com/library/windows/hardware/ff546606">HalGetBusDataByOffset</a> for the inputs <i>BusDataType</i> =  <b>EisaConfiguration</b> and <i>Offset</i> = 0, assuming the caller-allocated <i>Buffer</i> is of sufficient <i>Length</i>.</p>


## -syntax

````
typedef struct _CM_EISA_SLOT_INFORMATION {
  UCHAR  ReturnCode;
  UCHAR  ReturnFlags;
  UCHAR  MajorRevision;
  UCHAR  MinorRevision;
  USHORT Checksum;
  UCHAR  NumberFunctions;
  UCHAR  FunctionInformation;
  ULONG  CompressedId;
} CM_EISA_SLOT_INFORMATION, *PCM_EISA_SLOT_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>ReturnCode</b>

<dd>
<p>Contains a status code if an error occurs when the EISA BIOS is queried. Possible status codes include the following:</p>
<ul>
<li>EISA_INVALID_SLOT</li>
<li>EISA_INVALID_FUNCTION</li>
<li>EISA_INVALID_CONFIGURATION</li>
<li>EISA_EMPTY_SLOT</li>
<li>EISA_INVALID_BIOS_CALL</li>
</ul>
</dd>

### -field <b>ReturnFlags</b>

<dd>
<p>The return flags.</p>
</dd>

### -field <b>MajorRevision</b>

<dd>
<p>Information supplied by the manufacturer.</p>
</dd>

### -field <b>MinorRevision</b>

<dd>
<p>Information supplied by the manufacturer.</p>
</dd>

### -field <b>Checksum</b>

<dd>
<p>The checksum value, allowing validation of the configuration data.</p>
</dd>

### -field <b>NumberFunctions</b>

<dd>
<p>The number at this slot.</p>
</dd>

### -field <b>FunctionInformation</b>

<dd>
<p>Whether there is available <a href="https://msdn.microsoft.com/library/windows/hardware/ff541930">CM_EISA_FUNCTION_INFORMATION</a> for this slot.</p>
</dd>

### -field <b>CompressedId</b>

<dd>
<p>The EISA compressed identification of the device at this slot. This value is identical to the <b>CompressedId</b> member of the <b>CM_EISA_FUNCTION_INFORMATION</b> structure. This member can be read to determine whether the caller should call <b>HalGetBusData</b> or <b>HalGetBusDataByOffset</b> again with sufficient buffer space to get more detailed <b>CM_EISA_FUNCTION_INFORMATION</b> for a device it supports.</p>
</dd>
</dl>

## -remarks
<p>The information returned by <b>HalGetBusData</b> or <b>HalGetBusDataByOffset</b> in <b>CM_EISA_SLOT_INFORMATION</b> and in <b>CM_EISA_FUNCTION_INFORMATION</b> immediately following it is read-only.</p>

<p>The driver of an EISA device might call <b>HalGetBusData</b> or <b>HalGetBusDataByOffset</b> for each slot on each EISA bus in the system, requesting only <b>CM_EISA_SLOT_INFORMATION</b> in order to find the device(s) it supports by examining the returned <b>CompressedId</b> values. Then, such a driver could allocate sufficient buffer space to call <b>HalGetBusData(ByOffset)</b> again for <b>CM_EISA_SLOT_INFORMATION</b> and <b>CM_EISA_FUNCTION_INFORMATION</b> at slots where its device(s) can be found.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541930">CM_EISA_FUNCTION_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546599">HalGetBusData</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546606">HalGetBusDataByOffset</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20CM_EISA_SLOT_INFORMATION structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
