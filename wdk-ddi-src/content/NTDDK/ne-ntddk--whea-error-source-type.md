---
UID: NE.ntddk._WHEA_ERROR_SOURCE_TYPE
title: WHEA_ERROR_SOURCE_TYPE
author: windows-driver-content
description: The WHEA_ERROR_SOURCE_TYPE enumeration defines the different types of error sources that can report hardware errors.
old-location: whea\whea_error_source_type.htm
ms.assetid: d2615320-6c8a-4813-afb5-c5b510e5fde9
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: whea
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WHEA_ERROR_SOURCE_TYPE
req.alt-loc: ntddk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
ms.keywords: FILTER_INITIALIZATION_DATA, FILTER_INITIALIZATION_DATA, *PFILTER_INITIALIZATION_DATA
req.iface: 
---

# WHEA_ERROR_SOURCE_TYPE enumeration



## -description
<p>The WHEA_ERROR_SOURCE_TYPE enumeration defines the different types of error sources that can report hardware errors.</p>


## -syntax

````
typedef enum _WHEA_ERROR_SOURCE_TYPE { 
  WheaErrSrcTypeMCE         = 0x00,
  WheaErrSrcTypeCMC         = 0x01,
  WheaErrSrcTypeCPE         = 0x02,
  WheaErrSrcTypeNMI         = 0x03,
  WheaErrSrcTypePCIe        = 0x04,
  WheaErrSrcTypeGeneric     = 0x05,
  WheaErrSrcTypeINIT        = 0x06,
  WheaErrSrcTypeBOOT        = 0x07,
  WheaErrSrcTypeSCIGeneric  = 0x08,
  WheaErrSrcTypeIPFMCA      = 0x09,
  WheaErrSrcTypeIPFCMC      = 0x0a,
  WheaErrSrcTypeIPFCPE      = 0x0b,
  WheaErrSrcTypeMax
} WHEA_ERROR_SOURCE_TYPE, *PWHEA_ERROR_SOURCE_TYPE;
````


## -enum-fields
<dl>

### -field <a id="WheaErrSrcTypeMCE"></a><a id="wheaerrsrctypemce"></a><a id="WHEAERRSRCTYPEMCE"></a><b>WheaErrSrcTypeMCE</b>

<dd>
<p>A machine check exception (MCE).</p>
</dd>

### -field <a id="WheaErrSrcTypeCMC"></a><a id="wheaerrsrctypecmc"></a><a id="WHEAERRSRCTYPECMC"></a><b>WheaErrSrcTypeCMC</b>

<dd>
<p>A corrected machine check (CMC).</p>
</dd>

### -field <a id="WheaErrSrcTypeCPE"></a><a id="wheaerrsrctypecpe"></a><a id="WHEAERRSRCTYPECPE"></a><b>WheaErrSrcTypeCPE</b>

<dd>
<p>A corrected platform error (CPE).</p>
</dd>

### -field <a id="WheaErrSrcTypeNMI"></a><a id="wheaerrsrctypenmi"></a><a id="WHEAERRSRCTYPENMI"></a><b>WheaErrSrcTypeNMI</b>

<dd>
<p>A nonmaskable interrupt (NMI).</p>
</dd>

### -field <a id="WheaErrSrcTypePCIe"></a><a id="wheaerrsrctypepcie"></a><a id="WHEAERRSRCTYPEPCIE"></a><b>WheaErrSrcTypePCIe</b>

<dd>
<p>A PCI Express (PCIe) error.</p>
</dd>

### -field <a id="WheaErrSrcTypeGeneric"></a><a id="wheaerrsrctypegeneric"></a><a id="WHEAERRSRCTYPEGENERIC"></a><b>WheaErrSrcTypeGeneric</b>

<dd>
<p>A type of error source that does not conform to any of the other WHEA_ERROR_SOURCE_TYPE enumeration values.</p>
</dd>

### -field <a id="WheaErrSrcTypeINIT"></a><a id="wheaerrsrctypeinit"></a><a id="WHEAERRSRCTYPEINIT"></a><b>WheaErrSrcTypeINIT</b>

<dd>
<p>An Itanium processor INIT error.</p>
</dd>

### -field <a id="WheaErrSrcTypeBOOT"></a><a id="wheaerrsrctypeboot"></a><a id="WHEAERRSRCTYPEBOOT"></a><b>WheaErrSrcTypeBOOT</b>

<dd>
<p>A boot error source.</p>
</dd>

### -field <a id="WheaErrSrcTypeSCIGeneric"></a><a id="wheaerrsrctypescigeneric"></a><a id="WHEAERRSRCTYPESCIGENERIC"></a><b>WheaErrSrcTypeSCIGeneric</b>

<dd>
<p>A service control interrupt (SCI).</p>
</dd>

### -field <a id="WheaErrSrcTypeIPFMCA"></a><a id="wheaerrsrctypeipfmca"></a><a id="WHEAERRSRCTYPEIPFMCA"></a><b>WheaErrSrcTypeIPFMCA</b>

<dd>
<p>An Itanium processor machine check abort (MCA).</p>
</dd>

### -field <a id="WheaErrSrcTypeIPFCMC"></a><a id="wheaerrsrctypeipfcmc"></a><a id="WHEAERRSRCTYPEIPFCMC"></a><b>WheaErrSrcTypeIPFCMC</b>

<dd>
<p>An Itanium processor corrected machine check (CMC).</p>
</dd>

### -field <a id="WheaErrSrcTypeIPFCPE"></a><a id="wheaerrsrctypeipfcpe"></a><a id="WHEAERRSRCTYPEIPFCPE"></a><b>WheaErrSrcTypeIPFCPE</b>

<dd>
<p>An Itanium processor corrected platform error (CPE).</p>
</dd>

### -field <a id="WheaErrSrcTypeMax"></a><a id="wheaerrsrctypemax"></a><a id="WHEAERRSRCTYPEMAX"></a><b>WheaErrSrcTypeMax</b>

<dd>
<p>The maximum number of error source types that can report hardware errors.</p>
</dd>
</dl>

## -remarks
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff560505">WHEA_ERROR_SOURCE_DESCRIPTOR</a> structure contains a member of type WHEA_ERROR_SOURCE_TYPE that specifies the type of error source that is described by the structure.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff560465">WHEA_ERROR_PACKET</a> structure contains a member of type WHEA_ERROR_SOURCE_TYPE that specifies the type of error source that caused the error condition described by the structure.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff560505">WHEA_ERROR_SOURCE_DESCRIPTOR</a> structure contains a member of type WHEA_ERROR_SOURCE_TYPE that specifies the type of error source that is described by the structure.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff560465">WHEA_ERROR_PACKET</a> structure contains a member of type WHEA_ERROR_SOURCE_TYPE that specifies the type of error source that caused the error condition described by the structure.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff560505">WHEA_ERROR_SOURCE_DESCRIPTOR</a> structure contains a member of type WHEA_ERROR_SOURCE_TYPE that specifies the type of error source that is described by the structure.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff560465">WHEA_ERROR_PACKET</a> structure contains a member of type WHEA_ERROR_SOURCE_TYPE that specifies the type of error source that caused the error condition described by the structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560465">WHEA_ERROR_PACKET</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560505">WHEA_ERROR_SOURCE_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_ERROR_SOURCE_TYPE enumeration%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
