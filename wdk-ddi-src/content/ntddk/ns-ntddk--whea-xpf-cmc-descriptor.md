---
UID: NS.ntddk._WHEA_XPF_CMC_DESCRIPTOR
title: WHEA_XPF_CMC_DESCRIPTOR
author: windows-driver-content
description: The WHEA_XPF_CMC_DESCRIPTOR structure describes a corrected machine check (CMC) error source for an x86 or x64 processor.
old-location: whea\whea_xpf_cmc_descriptor.htm
old-project: whea
ms.assetid: d5eb2e20-9a11-4dae-9aa7-6e3799f0027f
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WHEA_XPF_CMC_DESCRIPTOR, WHEA_XPF_CMC_DESCRIPTOR, *PWHEA_XPF_CMC_DESCRIPTOR
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
req.alt-api: WHEA_XPF_CMC_DESCRIPTOR
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

# WHEA_XPF_CMC_DESCRIPTOR structure



## -description
<p>The WHEA_XPF_CMC_DESCRIPTOR structure describes a corrected machine check (CMC) error source for an x86 or x64 processor.</p>


## -syntax

````
typedef struct _WHEA_XPF_CMC_DESCRIPTOR {
  USHORT                       Type;
  BOOLEAN                      Enabled;
  UCHAR                        NumberOfBanks;
  ULONG                        Reserved;
  WHEA_NOTIFICATION_DESCRIPTOR Notify;
  WHEA_XPF_MC_BANK_DESCRIPTOR  Banks[WHEA_MAX_MC_BANKS];
} WHEA_XPF_CMC_DESCRIPTOR, *PWHEA_XPF_CMC_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>The type of error source descriptor. This member is always set to WHEA_ERROR_SOURCE_DESCRIPTOR_TYPE_XPFCMC.</p>
</dd>

### -field <b>Enabled</b>

<dd>
<p>A Boolean value that indicates if the error source is enabled.</p>
</dd>

### -field <b>NumberOfBanks</b>

<dd>
<p>The number of <a href="..\ntddk\ns-ntddk--whea-xpf-mc-bank-descriptor.md">WHEA_XPF_MC_BANK_DESCRIPTOR</a> structures contained in the <b>Banks</b> member.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>Notify</b>

<dd>
<p>A <a href="..\ntddk\ns-ntddk--whea-notification-descriptor.md">WHEA_NOTIFICATION_DESCRIPTOR</a> structure that describes the notification mechanism that is used by the error source.</p>
</dd>

### -field <b>Banks</b>

<dd>
<p>An array of <a href="..\ntddk\ns-ntddk--whea-xpf-mc-bank-descriptor.md">WHEA_XPF_MC_BANK_DESCRIPTOR</a> structures that describe the banks of machine check registers.</p>
</dd>
</dl>

## -remarks
<p>A WHEA_XPF_CMC_DESCRIPTOR structure is contained within the <a href="..\ntddk\ns-ntddk--whea-error-source-descriptor.md">WHEA_ERROR_SOURCE_DESCRIPTOR</a> structure.</p>

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
<a href="..\ntddk\ns-ntddk--whea-error-source-descriptor.md">WHEA_ERROR_SOURCE_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--whea-notification-descriptor.md">WHEA_NOTIFICATION_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--whea-xpf-mc-bank-descriptor.md">WHEA_XPF_MC_BANK_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_XPF_CMC_DESCRIPTOR structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
