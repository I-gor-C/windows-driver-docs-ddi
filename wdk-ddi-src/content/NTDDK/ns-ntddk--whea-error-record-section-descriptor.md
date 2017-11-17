---
UID: NS.ntddk._WHEA_ERROR_RECORD_SECTION_DESCRIPTOR
title: WHEA_ERROR_RECORD_SECTION_DESCRIPTOR
author: windows-driver-content
description: The WHEA_ERROR_RECORD_SECTION_DESCRIPTOR structure describes a section of error information that is part of an error record.
old-location: whea\whea_error_record_section_descriptor.htm
ms.assetid: f1abbf2b-19c9-4d34-9975-4f7ab98792af
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: whea
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WHEA_ERROR_RECORD_SECTION_DESCRIPTOR
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
req.irql: PASSIVE_LEVEL
ms.keywords: WHEA_ERROR_RECORD_SECTION_DESCRIPTOR, WHEA_ERROR_RECORD_SECTION_DESCRIPTOR, *PWHEA_ERROR_RECORD_SECTION_DESCRIPTOR
req.iface: 
---

# WHEA_ERROR_RECORD_SECTION_DESCRIPTOR structure



## -description
<p>The WHEA_ERROR_RECORD_SECTION_DESCRIPTOR structure describes a section of error information that is part of an <a href="https://msdn.microsoft.com/080da29a-b5cb-45a5-848d-048d9612ee2a">error record</a>.</p>


## -syntax

````
typedef struct _WHEA_ERROR_RECORD_SECTION_DESCRIPTOR {
  ULONG                                          SectionOffset;
  ULONG                                          SectionLength;
  WHEA_REVISION                                  Revision;
  WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS ValidBits;
  UCHAR                                          Reserved;
  WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_FLAGS     Flags;
  GUID                                           SectionType;
  GUID                                           FRUId;
  WHEA_ERROR_SEVERITY                            SectionSeverity;
  CCHAR                                          FRUText[20];
} WHEA_ERROR_RECORD_SECTION_DESCRIPTOR, *PWHEA_ERROR_RECORD_SECTION_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>SectionOffset</b>

<dd>
<p>The offset, in bytes, from the beginning of the error record to the beginning of the error record section.</p>
</dd>

### -field <b>SectionLength</b>

<dd>
<p>The length, in bytes, of the error data contained in the error record section.</p>
</dd>

### -field <b>Revision</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff560623">WHEA_REVISION</a> union that describes the revision level of the WHEA_ERROR_RECORD_SECTION_DESCRIPTOR structure.</p>
</dd>

### -field <b>ValidBits</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff560498">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS</a> union that specifies which members of this structure contain valid data.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_FLAGS union that describes the error record section. The WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_FLAGS union is defined as follows:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef union _WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_FLAGS {
  struct {
    ULONG  Primary:1;
    ULONG  ContainmentWarning:1;
    ULONG  Reset:1;
    ULONG  ThresholdExceeded:1;
    ULONG  ResourceNotAvailable:1;
    ULONG  LatentError:1;
    ULONG  Reserved:26;
  };
  ULONG  AsULONG;
} WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_FLAGS, *PWHEA_ERROR_RECORD_SECTION_DESCRIPTOR_FLAGS;</pre>
</td>
</tr>
</table></span></div>
<p></p>
<dl>

### -field <a id="Primary"></a><a id="primary"></a><a id="PRIMARY"></a><b>Primary</b>

<dd>
<p>A single bit that indicates that the corresponding error record section is the primary section within the error record. When there are multiple sections contained in an error record, the primary section is the section that is used for error recovery.</p>
</dd>

### -field <a id="ContainmentWarning"></a><a id="containmentwarning"></a><a id="CONTAINMENTWARNING"></a><b>ContainmentWarning</b>

<dd>
<p>A single bit that indicates that the error described by the corresponding error record section was not contained within the processor or memory hierarchy. In this situation, the error might have propagated to other components of the system.</p>
</dd>

### -field <a id="Reset"></a><a id="reset"></a><a id="RESET"></a><b>Reset</b>

<dd>
<p>A single bit that indicates that the component must be reinitialized or re-enabled by the operating system.</p>
</dd>

### -field <a id="ThresholdExceeded"></a><a id="thresholdexceeded"></a><a id="THRESHOLDEXCEEDED"></a><b>ThresholdExceeded</b>

<dd>
<p>A single bit that indicates that an error threshold has been exceeded.</p>
</dd>

### -field <a id="ResourceNotAvailable"></a><a id="resourcenotavailable"></a><a id="RESOURCENOTAVAILABLE"></a><b>ResourceNotAvailable</b>

<dd>
<p>A single bit that indicates that a resource could not be queried for error information due to conflicts with other system software or resources. In this situation, some of the fields of the corresponding error record section will be invalid.</p>
</dd>

### -field <a id="LatentError"></a><a id="latenterror"></a><a id="LATENTERROR"></a><b>LatentError</b>

<dd>
<p>A single bit that indicates that the reported error is a latent error (one not yet consumed) that could result in a more severe error when it is consumed.</p>
</dd>

### -field <a id="Reserved"></a><a id="reserved"></a><a id="RESERVED"></a><b>Reserved</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="AsULONG"></a><a id="asulong"></a><a id="ASULONG"></a><b>AsULONG</b>

<dd>
<p>A ULONG representation of the contents of the WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_FLAGS union.</p>
</dd>
</dl>
</dd>

### -field <b>SectionType</b>

<dd>
<p>A GUID that identifies the type of error data that is contained in the error record section. The standard section types are defined as follows:</p>
<p></p>
<dl>

### -field <a id="WHEA_PACKET_SECTION_GUID"></a><a id="whea_packet_section_guid"></a>WHEA_PACKET_SECTION_GUID

<dd>
<p>The error record section contains the hardware error packet that was passed to the operating system by the low-level hardware error handler (LLHEH) that reported the error. This data is described by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560465">WHEA_ERROR_PACKET</a> structure.</p>
</dd>

### -field <a id="PROCESSOR_GENERIC_ERROR_SECTION_GUID"></a><a id="processor_generic_error_section_guid"></a>PROCESSOR_GENERIC_ERROR_SECTION_GUID

<dd>
<p>The error record section contains processor error data that is not specific to a particular processor architecture. This data is described by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560607">WHEA_PROCESSOR_GENERIC_ERROR_SECTION</a> structure.</p>
</dd>

### -field <a id="IPF_PROCESSOR_ERROR_SECTION_GUID"></a><a id="ipf_processor_error_section_guid"></a>IPF_PROCESSOR_ERROR_SECTION_GUID

<dd>
<p>The error record section contains processor error data that is specific to the Itanium processor architecture. For more information about the format of the error data that is contained in this error record section, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=72212">Intel Itanium Processor Family System Abstraction Layer Specification</a>.</p>
</dd>

### -field <a id="FIRMWARE_ERROR_RECORD_REFERENCE_GUID"></a><a id="firmware_error_record_reference_guid"></a>FIRMWARE_ERROR_RECORD_REFERENCE_GUID

<dd>
<p>The error record section contains a reference to a firmware error record that is specific to the Itanium processor architecture. This data is described by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560520">WHEA_FIRMWARE_ERROR_RECORD_REFERENCE</a> structure.</p>
</dd>

### -field <a id="MEMORY_ERROR_SECTION_GUID"></a><a id="memory_error_section_guid"></a>MEMORY_ERROR_SECTION_GUID

<dd>
<p>The error record section contains platform memory error data. This data is described by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560565">WHEA_MEMORY_ERROR_SECTION</a> structure.</p>
</dd>

### -field <a id="NMI_SECTION_GUID"></a><a id="nmi_section_guid"></a>NMI_SECTION_GUID

<dd>
<p>The error record section contains nonmaskable interrupt (NMI) error data. This data is described by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560571">WHEA_NMI_ERROR_SECTION</a> structure.</p>
</dd>

### -field <a id="PCIEXPRESS_ERROR_SECTION_GUID"></a><a id="pciexpress_error_section_guid"></a>PCIEXPRESS_ERROR_SECTION_GUID

<dd>
<p>The error record section contains PCI Express (PCIe) error data. This data is described by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560576">WHEA_PCIEXPRESS_ERROR_SECTION</a> structure.</p>
</dd>

### -field <a id="PCIXBUS_ERROR_SECTION_GUID"></a><a id="pcixbus_error_section_guid"></a>PCIXBUS_ERROR_SECTION_GUID

<dd>
<p>The error record section contains PCI/PCI-X bus error data. This data is described by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560583">WHEA_PCIXBUS_ERROR_SECTION</a> structure.</p>
</dd>

### -field <a id="PCIXBUS_ERROR_SECTION_GUID"></a><a id="pcixbus_error_section_guid"></a>PCIXBUS_ERROR_SECTION_GUID

<dd>
<p>The error record section contains PCI/PCI-X device error data. This data is described by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560589">WHEA_PCIXDEVICE_ERROR_SECTION</a> structure.</p>
</dd>

### -field <a id="XPF_PROCESSOR_ERROR_SECTION_GUID"></a><a id="xpf_processor_error_section_guid"></a>XPF_PROCESSOR_ERROR_SECTION_GUID

<dd>
<p>The error record section contains processor error data that is specific to the x86 or x64 processor architecture. This data is described by a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560655">WHEA_XPF_PROCESSOR_ERROR_SECTION</a> structure.</p>
</dd>
</dl>
<p>For error record sections that do not conform to one of the standard section types, this member contains a platform-specific GUID that identifies the type of error data that is contained in the error record section. If a platform-specific GUID is not defined for the type of error data that is contained in the error record section, this member contains GENERIC_SECTION_GUID.</p>
</dd>

### -field <b>FRUId</b>

<dd>
<p>A GUID that identifies the Field Replaceable Unit (FRU) that contains the hardware where the error occurred. This member contains valid data only if the <b>ValidBits.FRUId</b> bit is set.</p>
</dd>

### -field <b>SectionSeverity</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff560503">WHEA_ERROR_SEVERITY</a>-typed value that indicates the severity of the error condition that is described by the error record section.</p>
</dd>

### -field <b>FRUText</b>

<dd>
<p>A character string that identifies the Field Replaceable Unit (FRU) that contains the hardware where the error occurred. This member contains valid data only if the <b>ValidBits.FRUText</b> bit is set.</p>
</dd>
</dl>

## -remarks
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/ff560483">WHEA_ERROR_RECORD</a> structure contains an array of WHEA_ERROR_RECORD_SECTION_DESCRIPTOR structures. Each descriptor describes a section of error information that is part of the error record.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560483">WHEA_ERROR_RECORD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560498">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR_VALIDBITS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560503">WHEA_ERROR_SEVERITY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560520">WHEA_FIRMWARE_ERROR_RECORD_REFERENCE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560607">WHEA_PROCESSOR_GENERIC_ERROR_SECTION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560565">WHEA_MEMORY_ERROR_SECTION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560571">WHEA_NMI_ERROR_SECTION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560576">WHEA_PCIEXPRESS_ERROR_SECTION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560583">WHEA_PCIXBUS_ERROR_SECTION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560589">WHEA_PCIXDEVICE_ERROR_SECTION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560623">WHEA_REVISION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560655">WHEA_XPF_PROCESSOR_ERROR_SECTION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_ERROR_RECORD_SECTION_DESCRIPTOR structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
