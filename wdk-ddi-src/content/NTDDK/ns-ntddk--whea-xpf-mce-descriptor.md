---
UID: NS.ntddk._WHEA_XPF_MCE_DESCRIPTOR
title: WHEA_XPF_MCE_DESCRIPTOR
author: windows-driver-content
description: The WHEA_XPF_MCE_DESCRIPTOR structure describes a machine check exception (MCE) error source for an x86 or x64 processor.
old-location: whea\whea_xpf_mce_descriptor.htm
ms.assetid: cdf52fe7-40ac-4baf-aaa0-c23b40574376
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
req.alt-api: WHEA_XPF_MCE_DESCRIPTOR
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
ms.keywords: WHEA_XPF_MCE_DESCRIPTOR, WHEA_XPF_MCE_DESCRIPTOR, *PWHEA_XPF_MCE_DESCRIPTOR
req.iface: 
---

# WHEA_XPF_MCE_DESCRIPTOR structure



## -description
<p>The WHEA_XPF_MCE_DESCRIPTOR structure describes a machine check exception (MCE) error source for an x86 or x64 processor.</p>


## -syntax

````
typedef struct _WHEA_XPF_MCE_DESCRIPTOR {
  USHORT                      Type;
  UCHAR                       Enabled;
  UCHAR                       NumberOfBanks;
  XPF_MCE_FLAGS               Flags;
  ULONGLONG                   MCG_Capability;
  ULONGLONG                   MCG_GlobalControl;
  WHEA_XPF_MC_BANK_DESCRIPTOR Banks[WHEA_MAX_MC_BANKS];
} WHEA_XPF_MCE_DESCRIPTOR, *PWHEA_XPF_MCE_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>The type of error source descriptor. This member is always set to WHEA_ERROR_SOURCE_DESCRIPTOR_TYPE_XPFMCE.</p>
</dd>

### -field <b>Enabled</b>

<dd>
<p>A Boolean value that indicates if the error source is enabled.</p>
</dd>

### -field <b>NumberOfBanks</b>

<dd>
<p>The number of <a href="https://msdn.microsoft.com/library/windows/hardware/ff560651">WHEA_XPF_MC_BANK_DESCRIPTOR</a> structures contained in the <b>Banks</b> member.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>An XPF_MCE_FLAGS union that indicates which of the members of the WHEA_XPF_MCE_DESCRIPTOR structure can be written to by the operating system. The XPF_MCE_FLAGS union is defined as follows:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef union _XPF_MCE_FLAGS {
  struct {
    UCHAR  MCG_CapabilityRW:1;
    UCHAR  MCG_GlobalControlRW:1;
    UCHAR  Reserved:30;
  };
  UCHAR  AsULONG;
} XPF_MCE_FLAGS, *PXPF_MCE_FLAGS;</pre>
</td>
</tr>
</table></span></div>
<p></p>
<dl>

### -field <a id="MCG_CapabilityRW"></a><a id="mcg_capabilityrw"></a><a id="MCG_CAPABILITYRW"></a><b>MCG_CapabilityRW</b>

<dd>
<p>A single bit that indicates that the operating system can write to the <b>MCG_Capability</b> member of the WHEA_XPF_MCE_DESCRIPTOR structure.</p>
</dd>

### -field <a id="MCG_GlobalControlRW"></a><a id="mcg_globalcontrolrw"></a><a id="MCG_GLOBALCONTROLRW"></a><b>MCG_GlobalControlRW</b>

<dd>
<p>A single bit that indicates that the operating system can write to the <b>MCG_GlobalControl</b> member of the WHEA_XPF_MCE_DESCRIPTOR structure.</p>
</dd>

### -field <a id="Reserved"></a><a id="reserved"></a><a id="RESERVED"></a><b>Reserved</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <a id="AsULONG"></a><a id="asulong"></a><a id="ASULONG"></a><b>AsULONG</b>

<dd>
<p>A ULONG representation of the contents of the XPF_MCE_FLAGS union.</p>
</dd>
</dl>
</dd>

### -field <b>MCG_Capability</b>

<dd>
<p>The contents of the processor's IA32_MCG_CAP model-specific register. This register contains capability information about the machine check architecture of the processor. For more information about the IA32_MCG_CAP register, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=78804">Intel 64 and IA-32 Architectures Software Developer's Manual</a>.</p>
</dd>

### -field <b>MCG_GlobalControl</b>

<dd>
<p>The contents of the processor's IA32_MCG_CTL model-specific register. This register controls the reporting of machine check exceptions. For more information about the IA32_MCG_CTL register, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=78804">Intel 64 and IA-32 Architectures Software Developer's Manual</a>.</p>
</dd>

### -field <b>Banks</b>

<dd>
<p>An array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff560651">WHEA_XPF_MC_BANK_DESCRIPTOR</a> structures that describe the banks of machine check registers.</p>
</dd>
</dl>

## -remarks
<p>A WHEA_XPF_MCE_DESCRIPTOR structure is contained within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560505">WHEA_ERROR_SOURCE_DESCRIPTOR</a> structure.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560505">WHEA_ERROR_SOURCE_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560651">WHEA_XPF_MC_BANK_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_XPF_MCE_DESCRIPTOR structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
