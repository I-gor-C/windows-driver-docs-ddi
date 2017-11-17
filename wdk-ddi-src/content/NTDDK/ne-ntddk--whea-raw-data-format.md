---
UID: NE.ntddk._WHEA_RAW_DATA_FORMAT
title: WHEA_RAW_DATA_FORMAT
author: windows-driver-content
description: The WHEA_RAW_DATA_FORMAT enumeration defines the possible formats that raw hardware error data can be encoded in a hardware error packet.
old-location: whea\whea_raw_data_format.htm
ms.assetid: 809f2d72-e769-48c1-9ecf-6fa9020f6cdb
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
req.alt-api: WHEA_RAW_DATA_FORMAT
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

# WHEA_RAW_DATA_FORMAT enumeration



## -description
<p>The WHEA_RAW_DATA_FORMAT enumeration defines the possible formats that raw hardware error data can be encoded in a hardware error packet.</p>


## -syntax

````
typedef enum _WHEA_RAW_DATA_FORMAT { 
  WheaRawDataFormatIPFSalRecord  = 0x00,
  WheaRawDataFormatIA32MCA,
  WheaRawDataFormatIntel64MCA,
  WheaRawDataFormatAMD64MCA,
  WheaRawDataFormatMemory,
  WheaRawDataFormatPCIExpress,
  WheaRawDataFormatNMIPort,
  WheaRawDataFormatPCIXBus,
  WheaRawDataFormatPCIXDevice,
  WheaRawDataFormatGeneric,
  WheaRawDataFormatMax
} WHEA_RAW_DATA_FORMAT, *PWHEA_RAW_DATA_FORMAT;
````


## -enum-fields
<dl>

### -field <a id="WheaRawDataFormatIPFSalRecord"></a><a id="whearawdataformatipfsalrecord"></a><a id="WHEARAWDATAFORMATIPFSALRECORD"></a><b>WheaRawDataFormatIPFSalRecord</b>

<dd>
<p>The raw data in the hardware error packet contains an Itanium processor family system abstraction layer (SAL) error record. For more information about the format of a SAL error record, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=72212">Intel Itanium Processor Family System Abstraction Layer Specification</a>.</p>
</dd>

### -field <a id="WheaRawDataFormatIA32MCA"></a><a id="whearawdataformatia32mca"></a><a id="WHEARAWDATAFORMATIA32MCA"></a><b>WheaRawDataFormatIA32MCA</b>

<dd>
<p>The raw data in the hardware error packet contains an MCA_EXCEPTION structure. For more information about the MCA_EXCEPTION structure, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540659">HalQuerySystemInformation</a>.</p>
</dd>

### -field <a id="WheaRawDataFormatIntel64MCA"></a><a id="whearawdataformatintel64mca"></a><a id="WHEARAWDATAFORMATINTEL64MCA"></a><b>WheaRawDataFormatIntel64MCA</b>

<dd>
<p>The raw data in the hardware error packet contains an MCA_EXCEPTION structure. For more information about the MCA_EXCEPTION structure, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540659">HalQuerySystemInformation</a>.</p>
</dd>

### -field <a id="WheaRawDataFormatAMD64MCA"></a><a id="whearawdataformatamd64mca"></a><a id="WHEARAWDATAFORMATAMD64MCA"></a><b>WheaRawDataFormatAMD64MCA</b>

<dd>
<p>The raw data in the hardware error packet contains an MCA_EXCEPTION structure. For more information about the MCA_EXCEPTION structure, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540659">HalQuerySystemInformation</a>.</p>
</dd>

### -field <a id="WheaRawDataFormatMemory"></a><a id="whearawdataformatmemory"></a><a id="WHEARAWDATAFORMATMEMORY"></a><b>WheaRawDataFormatMemory</b>

<dd>
<p>The raw data in the hardware error packet contains memory error data. The format of this error data is memory architecture-dependent.</p>
</dd>

### -field <a id="WheaRawDataFormatPCIExpress"></a><a id="whearawdataformatpciexpress"></a><a id="WHEARAWDATAFORMATPCIEXPRESS"></a><b>WheaRawDataFormatPCIExpress</b>

<dd>
<p>The raw data in the hardware error packet contains a <a href="https://msdn.microsoft.com/library/windows/hardware/ff537457">PCI_EXPRESS_AER_CAPABILITY</a> structure.</p>
</dd>

### -field <a id="WheaRawDataFormatNMIPort"></a><a id="whearawdataformatnmiport"></a><a id="WHEARAWDATAFORMATNMIPORT"></a><b>WheaRawDataFormatNMIPort</b>

<dd>
<p>The raw data in the hardware error packet contains the data that was read from the nonmaskable interrupt (NMI) I/O ports by the NMI low-level hardware error handler (LLHEH).</p>
</dd>

### -field <a id="WheaRawDataFormatPCIXBus"></a><a id="whearawdataformatpcixbus"></a><a id="WHEARAWDATAFORMATPCIXBUS"></a><b>WheaRawDataFormatPCIXBus</b>

<dd>
<p>The raw data in the hardware error packet contains PCI/PCI-X bus error data. The format of this error data is specific to the implementation.</p>
</dd>

### -field <a id="WheaRawDataFormatPCIXDevice"></a><a id="whearawdataformatpcixdevice"></a><a id="WHEARAWDATAFORMATPCIXDEVICE"></a><b>WheaRawDataFormatPCIXDevice</b>

<dd>
<p>The raw data in the hardware error packet contains a PCI/PCI-X device error data. The format of this error data is specific to the implementation.</p>
</dd>

### -field <a id="WheaRawDataFormatGeneric"></a><a id="whearawdataformatgeneric"></a><a id="WHEARAWDATAFORMATGENERIC"></a><b>WheaRawDataFormatGeneric</b>

<dd>
<p>The raw data in the hardware error packet contains a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560524">WHEA_GENERIC_ERROR</a> structure.</p>
</dd>

### -field <a id="WheaRawDataFormatMax"></a><a id="whearawdataformatmax"></a><a id="WHEARAWDATAFORMATMAX"></a><b>WheaRawDataFormatMax</b>

<dd>
<p>The maximum number of formats of raw hardware error data.</p>
</dd>
</dl>

## -remarks
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff560476">WHEA_ERROR_PACKET_V1</a> structure contains a member of type WHEA_RAW_DATA_FORMAT that specifies the format of the raw data that is contained in the hardware error packet.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff560476">WHEA_ERROR_PACKET_V1</a> structure contains a member of type WHEA_RAW_DATA_FORMAT that specifies the format of the raw data that is contained in the hardware error packet.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff560476">WHEA_ERROR_PACKET_V1</a> structure contains a member of type WHEA_RAW_DATA_FORMAT that specifies the format of the raw data that is contained in the hardware error packet.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540659">HalQuerySystemInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537457">PCI_EXPRESS_AER_CAPABILITY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560476">WHEA_ERROR_PACKET_V1</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560524">WHEA_GENERIC_ERROR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_RAW_DATA_FORMAT enumeration%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
