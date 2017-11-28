---
UID: NS.wdm._CM_EISA_FUNCTION_INFORMATION
title: CM_EISA_FUNCTION_INFORMATION
author: windows-driver-content
description: The CM_EISA_FUNCTION_INFORMATION structure defines detailed EISA configuration information returned by HalGetBusData for the input BusDataType EisaConfiguration, or by HalGetBusDataByOffset for the input BusDataType EisaConfiguration and the Offset zero, assuming the caller-allocated Buffer is of sufficient Length.
old-location: kernel\cm_eisa_function_information.htm
old-project: kernel
ms.assetid: 06034776-4faf-4918-b9ec-bc095455cf14
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: CM_EISA_FUNCTION_INFORMATION, CM_EISA_FUNCTION_INFORMATION, *PCM_EISA_FUNCTION_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CM_EISA_FUNCTION_INFORMATION
req.alt-loc: wdm.h
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
req.iface: 
req.product: Windows 10 or later.
---

# CM_EISA_FUNCTION_INFORMATION structure



## -description
<p>The <b>CM_EISA_FUNCTION_INFORMATION</b> structure defines detailed EISA configuration information returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff546599">HalGetBusData</a> for the input <i>BusDataType </i><b>EisaConfiguration</b>, or by <b>HalGetBusDataByOffset</b> for the input <i>BusDataType </i><b>EisaConfiguration</b> and the <i>Offset</i> zero, assuming the caller-allocated <i>Buffer</i> is of sufficient <i>Length</i>.</p>


## -syntax

````
typedef struct _CM_EISA_FUNCTION_INFORMATION {
  ULONG                     CompressedId;
  UCHAR                     IdSlotFlags1;
  UCHAR                     IdSlotFlags2;
  UCHAR                     MinorRevision;
  UCHAR                     MajorRevision;
  UCHAR                     Selections[26];
  UCHAR                     FunctionFlags;
  UCHAR                     TypeString[80];
  EISA_MEMORY_CONFIGURATION EisaMemory[9];
  EISA_IRQ_CONFIGURATION    EisaIrq[7];
  EISA_DMA_CONFIGURATION    EisaDma[4];
  EISA_PORT_CONFIGURATION   EisaPort[20];
  UCHAR                     InitializationData[60];
} CM_EISA_FUNCTION_INFORMATION, *PCM_EISA_FUNCTION_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>CompressedId</b>

<dd>
<p>The EISA compressed identification of the device at this slot. The value is identical to the <b>CompressedId</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541941">CM_EISA_SLOT_INFORMATION</a> structure.</p>
</dd>

### -field <b>IdSlotFlags1</b>

<dd>
<p>The EISA slot identification flags.</p>
</dd>

### -field <b>IdSlotFlags2</b>

<dd>
<p>The EISA slot identification flags.</p>
</dd>

### -field <b>MinorRevision</b>

<dd>
<p>Information supplied by the manufacturer. </p>
</dd>

### -field <b>MajorRevision</b>

<dd>
<p>Information supplied by the manufacturer. </p>
</dd>

### -field <b>Selections</b>

<dd>
<p>The EISA selections for the device.</p>
</dd>

### -field <b>FunctionFlags</b>

<dd>
<p>Indicates which of the members has available information. Callers can use the following system-defined masks to determine whether a particular type of configuration information can be or has been returned by <b>HalGetBusData</b> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff546606">HalGetBusDataByOffset</a>:</p>
<dl>
<dd>
<p>EISA_FUNCTION_ENABLED</p>
</dd>
<dd>
<p>EISA_FREE_FORM_DATA</p>
</dd>
<dd>
<p>EISA_HAS_PORT_INIT_ENTRY</p>
</dd>
<dd>
<p>EISA_HAS_PORT_RANGE</p>
</dd>
<dd>
<p>EISA_HAS_DMA_ENTRY</p>
</dd>
<dd>
<p>EISA_HAS_IRQ_ENTRY</p>
</dd>
<dd>
<p>EISA_HAS_MEMORY_ENTRY</p>
</dd>
<dd>
<p>EISA_HAS_TYPE_ENTRY</p>
</dd>
<dd>
<p>EISA_HAS_INFORMATION</p>
</dd>
</dl>
<p>The EISA_HAS_INFORMATION mask is a combination of the following:</p>
<dl>
<dd>
<p>EISA_HAS_PORT_RANGE</p>
</dd>
<dd>
<p>EISA_HAS_DMA_ENTRY</p>
</dd>
<dd>
<p>EISA_HAS_IRQ_ENTRY</p>
</dd>
<dd>
<p>EISA_HAS_MEMORY_ENTRY</p>
</dd>
<dd>
<p>EISA_HAS_TYPE_ENTRY</p>
</dd>
</dl>
</dd>

### -field <b>TypeString</b>

<dd>
<p>Specifies the type of device.</p>
</dd>

### -field <b>EisaMemory</b>

<dd>
<p>Describes the EISA device memory configuration information, defined as follows:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef struct _EISA_MEMORY_CONFIGURATION {
    EISA_MEMORY_TYPE ConfigurationByte;
    UCHAR DataSize;
    USHORT AddressLowWord;
    UCHAR AddressHighByte;
    USHORT MemorySize;
} EISA_MEMORY_CONFIGURATION, *PEISA_MEMORY_CONFIGURATION;</pre>
</td>
</tr>
</table></span></div>
</dd>

### -field <b>EisaIrq</b>

<dd>
<p>Describes the EISA interrupt configuration information, defined as follows:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef struct _EISA_IRQ_CONFIGURATION {
    EISA_IRQ_DESCRIPTOR ConfigurationByte;
    UCHAR Reserved;
} EISA_IRQ_CONFIGURATION, *PEISA_IRQ_CONFIGURATION;</pre>
</td>
</tr>
</table></span></div>
</dd>

### -field <b>EisaDma</b>

<dd>
<p>Describes the EISA DMA configuration information, defined as follows:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef struct _EISA_DMA_CONFIGURATION {
    DMA_CONFIGURATION_BYTE0 ConfigurationByte0;
    DMA_CONFIGURATION_BYTE1 ConfigurationByte1;
} EISA_DMA_CONFIGURATION, *PEISA_DMA_CONFIGURATION;</pre>
</td>
</tr>
</table></span></div>
</dd>

### -field <b>EisaPort</b>

<dd>
<p>Describes the EISA device port configuration information, defined as follows:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef struct _EISA_PORT_CONFIGURATION {
    EISA_PORT_DESCRIPTOR Configuration;
    USHORT PortAddress;
} EISA_PORT_CONFIGURATION, *PEISA_PORT_CONFIGURATION;</pre>
</td>
</tr>
</table></span></div>
</dd>

### -field <b>InitializationData</b>

<dd>
<p>Vendor-supplied, device-specific initialization data, if any. </p>
</dd>
</dl>

## -remarks
<p>The information returned by <b>HalGetBusData</b> or <b>HalGetBusDataByOffset</b> in <b>CM_EISA_FUNCTION_INFORMATION</b> and/or in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541941">CM_EISA_SLOT_INFORMATION</a> header immediately preceding it is read-only.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541941">CM_EISA_SLOT_INFORMATION</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20CM_EISA_FUNCTION_INFORMATION structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
