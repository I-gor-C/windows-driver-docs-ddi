---
UID: NS.ntddk._WHEA_ERROR_SOURCE_DESCRIPTOR
title: WHEA_ERROR_SOURCE_DESCRIPTOR
author: windows-driver-content
description: The WHEA_ERROR_SOURCE_DESCRIPTOR structure describes an error source.
old-location: whea\whea_error_source_descriptor.htm
old-project: whea
ms.assetid: 59ee6d51-c60a-4a71-b831-1b9437a69d34
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WHEA_ERROR_SOURCE_DESCRIPTOR,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WHEA_ERROR_SOURCE_DESCRIPTOR
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
req.iface: 
---

# WHEA_ERROR_SOURCE_DESCRIPTOR structure



## -description
<p>The WHEA_ERROR_SOURCE_DESCRIPTOR structure describes an error source.</p>


## -syntax

````
typedef struct _WHEA_ERROR_SOURCE_DESCRIPTOR {
  ULONG                   Length;
  ULONG                   Version;
  WHEA_ERROR_SOURCE_TYPE  Type;
  WHEA_ERROR_SOURCE_STATE State;
  ULONG                   MaxRawDataLength;
  ULONG                   NumRecordsToPreallocate;
  ULONG                   MaxSectionsPerRecord;
  ULONG                   ErrorSourceId;
  ULONG                   PlatformErrorSourceId;
  ULONG                   Flags;
  union {
    WHEA_XPF_MCE_DESCRIPTOR       XpfMceDescriptor;
    WHEA_XPF_CMC_DESCRIPTOR       XpfCmcDescriptor;
    WHEA_XPF_NMI_DESCRIPTOR       XpfNmiDescriptor;
    WHEA_IPF_MCA_DESCRIPTOR       IpfMcaDescriptor;
    WHEA_IPF_CMC_DESCRIPTOR       IpfCmcDescriptor;
    WHEA_IPF_CPE_DESCRIPTOR       IpfCpeDescriptor;
    WHEA_AER_ROOTPORT_DESCRIPTOR  AerRootportDescriptor;
    WHEA_AER_ENDPOINT_DESCRIPTOR  AerEndpointDescriptor;
    WHEA_AER_BRIDGE_DESCRIPTOR    AerBridgeDescriptor;
    WHEA_GENERIC_ERROR_DESCRIPTOR GenErrDescriptor;
  } Info;
} WHEA_ERROR_SOURCE_DESCRIPTOR, *PWHEA_ERROR_SOURCE_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>Length</b>

<dd>
<p>The size, in bytes, of the WHEA_ERROR_SOURCE_DESCRIPTOR structure.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>The version number of the WHEA_ERROR_SOURCE_DESCRIPTOR structure. This member contains the value WHEA_ERROR_SOURCE_DESCRIPTOR_VERSION_10.</p>
</dd>

### -field <b>Type</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff560511">WHEA_ERROR_SOURCE_TYPE</a>-typed value that specifies the type of the error source.</p>
</dd>

### -field <b>State</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff560507">WHEA_ERROR_SOURCE_STATE</a>-typed value that specifies the state of the error source.</p>
</dd>

### -field <b>MaxRawDataLength</b>

<dd>
<p>The maximum number of bytes of raw data included in a hardware error packet that is reported by this error source. This number must be large enough to include any additional platform-specific error information that is added to the hardware error packet by the PSHED or by a PSHED plug-in.</p>
</dd>

### -field <b>NumRecordsToPreallocate</b>

<dd>
<p>The number of error records that should be pre-allocated for hardware errors that are reported by this error source.</p>
</dd>

### -field <b>MaxSectionsPerRecord</b>

<dd>
<p>The maximum number of error record sections that are required in an error record to describe a hardware error that is reported by this error source. This number must be large enough to include any additional error record sections that are added to the error record by the PSHED or by a PSHED plug-in during the processing of the error.</p>
</dd>

### -field <b>ErrorSourceId</b>

<dd>
<p>The identifier of the error source. This identifier is unique only on the system where the error source exists.</p>
</dd>

### -field <b>PlatformErrorSourceId</b>

<dd>
<p>The identifier of the error source as enumerated by the hardware platform. This identifier is unique only on the system where the error source exists.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A bitwise OR'ed combination of flags that describes the error source. Possible flags are:</p>
<p></p>
<dl>

### -field <a id="WHEA_ERROR_SOURCE_FLAG_DEFAULTSOURCE"></a><a id="whea_error_source_flag_defaultsource"></a>WHEA_ERROR_SOURCE_FLAG_DEFAULTSOURCE

<dd>
<p>This flag indicates that the error source is a default error source for the type of hardware platform on which it exists.</p>
</dd>

### -field <a id="WHEA_ERROR_SOURCE_FLAG_FIRMWAREFIRST"></a><a id="whea_error_source_flag_firmwarefirst"></a>WHEA_ERROR_SOURCE_FLAG_FIRMWAREFIRST

<dd>
<p>This flag indicates that the errors that are reported by this error source are handled by the firmware before control of the hardware error processing is passed to the operating system.</p>
</dd>

### -field <a id="WHEA_ERROR_SOURCE_FLAG_GLOBAL"></a><a id="whea_error_source_flag_global"></a>WHEA_ERROR_SOURCE_FLAG_GLOBAL

<dd>
<p>This flag indicates that the settings specified for the error source are to be applied to all of the error sources in the system that are of the same type as that specified in the <b>Type</b> member.</p>
</dd>
</dl>
</dd>

### -field <b>Info</b>

<dd>
<p>A union of descriptor structures that are specific to each different type of error source.</p>
<dl>

### -field <b>XpfMceDescriptor</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff560649">WHEA_XPF_MCE_DESCRIPTOR</a> structure that describes an x86 or x64 processor machine check exception (MCE) error source.</p>
</dd>

### -field <b>XpfCmcDescriptor</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff560646">WHEA_XPF_CMC_DESCRIPTOR</a> structure that describes an x86 or x64 processor corrected machine check (CMC) error source.</p>
</dd>

### -field <b>XpfNmiDescriptor</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff560654">WHEA_XPF_NMI_DESCRIPTOR</a> structure that describes an x86 or x64 processor nonmaskable interrupt (NMI) error source.</p>
</dd>

### -field <b>IpfMcaDescriptor</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff560552">WHEA_IPF_MCA_DESCRIPTOR</a> structure that describes an Itanium processor machine check abort (MCA) error source.</p>
</dd>

### -field <b>IpfCmcDescriptor</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff560549">WHEA_IPF_CMC_DESCRIPTOR</a> structure that describes an Itanium processor corrected machine check (CMC) error source.</p>
</dd>

### -field <b>IpfCpeDescriptor</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff560550">WHEA_IPF_CPE_DESCRIPTOR</a> structure that describes an Itanium processor corrected platform error (CPE) error source.</p>
</dd>

### -field <b>AerRootportDescriptor</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff560450">WHEA_AER_ROOTPORT_DESCRIPTOR</a> structure that describes a PCI Express (PCIe) root port error source.</p>
</dd>

### -field <b>AerEndpointDescriptor</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff560447">WHEA_AER_ENDPOINT_DESCRIPTOR</a> structure that describes a PCIe endpoint error source. </p>
</dd>

### -field <b>AerBridgeDescriptor</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff560446">WHEA_AER_BRIDGE_DESCRIPTOR</a> structure that describes a PCIe bridge error source.</p>
</dd>

### -field <b>GenErrDescriptor</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff560531">WHEA_GENERIC_ERROR_DESCRIPTOR</a> structure that describes a generic error source.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The WHEA_ERROR_SOURCE_DESCRIPTOR structure describes an error source. The WHEA_ERROR_SOURCE_DESCRIPTOR structure is also used to configure an error source.</p>

<p>A user-mode WHEA management application can control the error sources in the system by calling the methods in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559521">WHEAErrorSourceMethods</a> WMI provider class.</p>

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
<a href="..\ntddk\nc-ntddk-pshed-pi-disable-error-source.md">DisableErrorSource</a>
</dt>
<dt>
<a href="..\ntddk\nc-ntddk-pshed-pi-enable-error-source.md">EnableErrorSource</a>
</dt>
<dt>
<a href="..\ntddk\nc-ntddk-pshed-pi-get-all-error-sources.md">GetAllErrorSources</a>
</dt>
<dt>
<a href="..\ntddk\nc-ntddk-pshed-pi-get-error-source-info.md">GetErrorSourceInfo</a>
</dt>
<dt>
<a href="..\ntddk\nc-ntddk-pshed-pi-set-error-source-info.md">SetErrorSourceInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559523">WHEAErrorSourceMethods::DisableErrorSourceRtn</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559525">WHEAErrorSourceMethods::EnableErrorSourceRtn</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559527">WHEAErrorSourceMethods::GetAllErrorSourcesRtn</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559530">WHEAErrorSourceMethods::GetErrorSourceInfoRtn</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559531">WHEAErrorSourceMethods::SetErrorSourceInfoRtn</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560446">WHEA_AER_BRIDGE_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560447">WHEA_AER_ENDPOINT_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560450">WHEA_AER_ROOTPORT_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560507">WHEA_ERROR_SOURCE_STATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560511">WHEA_ERROR_SOURCE_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560531">WHEA_GENERIC_ERROR_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560549">WHEA_IPF_CMC_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560550">WHEA_IPF_CPE_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560552">WHEA_IPF_MCA_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560646">WHEA_XPF_CMC_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560649">WHEA_XPF_MCE_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560654">WHEA_XPF_NMI_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_ERROR_SOURCE_DESCRIPTOR structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
