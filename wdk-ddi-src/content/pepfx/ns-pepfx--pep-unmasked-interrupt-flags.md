---
UID: NS.pepfx._PEP_UNMASKED_INTERRUPT_FLAGS
title: PEP_UNMASKED_INTERRUPT_FLAGS
author: windows-driver-content
description: The PEP_UNMASKED_INTERRUPT_FLAGS union indicates whether an unmasked interrupt source is a primary interrupt or a secondary interrupt.
old-location: kernel\pep_unmasked_interrupt_flags.htm
old-project: kernel
ms.assetid: A385FBF9-2222-49E0-A708-1638C0D2FF7A
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PEP_UNMASKED_INTERRUPT_FLAGS, PEP_UNMASKED_INTERRUPT_FLAGS, *PPEP_UNMASKED_INTERRUPT_FLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_UNMASKED_INTERRUPT_FLAGS
req.alt-loc: pepfx.h
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

# PEP_UNMASKED_INTERRUPT_FLAGS structure



## -description
<p>The <b>PEP_UNMASKED_INTERRUPT_FLAGS</b> union indicates whether an unmasked interrupt source is a primary interrupt or a secondary interrupt.</p>


## -syntax

````
typedef union _PEP_UNMASKED_INTERRUPT_FLAGS {
  struct {
    USHORT SecondaryInterrupt  :1;
    USHORT Reserved  :15;
  };
  USHORT AsUSHORT;
} PEP_UNMASKED_INTERRUPT_FLAGS;
````


## -struct-fields
<dl>

### -field ( <i>unnamed struct</i> )

<dd>
<p>A structure that contains the bitfields for the individual unmasked interrupt flags.</p>
<dl>

### -field <b>SecondaryInterrupt</b>

<dd>
<p>Whether this interrupt is a primary interrupt or a secondary interrupt. This bitfield is 0 if the interrupt source is a primary interrupt, and is 1 is the interrupt source is a secondary interrupt. For more information, see <a href="NULL">Primary and Secondary Interrupts</a>.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for future use.</p>
</dd>
</dl>
</dd>

### -field <b>AsUSHORT</b>

<dd>
<p>A USHORT value that contains all of the unmasked interrupt flags.</p>
</dd>
</dl>

## -remarks
<p>The <b>Flags</b> member of the <a href="..\pepfx\ns-pepfx--pep-unmasked-interrupt-information.md">PEP_UNMASKED_INTERRUPT_INFORMATION</a> structure is a <b>PEP_UNMASKED_INTERRUPT_FLAGS</b> union.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with Windows 10.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Pepfx.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\pepfx\ns-pepfx--pep-unmasked-interrupt-information.md">PEP_UNMASKED_INTERRUPT_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_UNMASKED_INTERRUPT_FLAGS union%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
