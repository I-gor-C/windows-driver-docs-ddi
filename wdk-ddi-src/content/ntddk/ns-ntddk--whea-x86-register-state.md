---
UID: NS.ntddk._WHEA_X86_REGISTER_STATE
title: WHEA_X86_REGISTER_STATE
author: windows-driver-content
description: The WHEA_X86_REGISTER_STATE structure describes the state of an x86 processor's registers.
old-location: whea\whea_x86_register_state.htm
old-project: whea
ms.assetid: 64079b03-9771-4940-a19e-a29389cbf2fe
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WHEA_X86_REGISTER_STATE, WHEA_X86_REGISTER_STATE, *PWHEA_X86_REGISTER_STATE
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
req.alt-api: WHEA_X86_REGISTER_STATE
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

# WHEA_X86_REGISTER_STATE structure



## -description
<p>The WHEA_X86_REGISTER_STATE structure describes the state of an x86 processor's registers.</p>


## -syntax

````
typedef struct _WHEA_X86_REGISTER_STATE {
  ULONG     Eax;
  ULONG     Ebx;
  ULONG     Ecx;
  ULONG     Edx;
  ULONG     Esi;
  ULONG     Edi;
  ULONG     Ebp;
  ULONG     Esp;
  USHORT    Cs;
  USHORT    Ds;
  USHORT    Ss;
  USHORT    Es;
  USHORT    Fs;
  USHORT    Gs;
  ULONG     Eflags;
  ULONG     Eip;
  ULONG     Cr0;
  ULONG     Cr1;
  ULONG     Cr2;
  ULONG     Cr3;
  ULONG     Cr4;
  ULONGLONG Gdtr;
  ULONGLONG Idtr;
  USHORT    Ldtr;
  USHORT    Tr;
} WHEA_X86_REGISTER_STATE, *PWHEA_X86_REGISTER_STATE;
````


## -struct-fields
<dl>

### -field <b>Eax</b>

<dd>
<p>The accumulator register.</p>
</dd>

### -field <b>Ebx</b>

<dd>
<p>The base register.</p>
</dd>

### -field <b>Ecx</b>

<dd>
<p>The count register.</p>
</dd>

### -field <b>Edx</b>

<dd>
<p>The data register.</p>
</dd>

### -field <b>Esi</b>

<dd>
<p>The source index register.</p>
</dd>

### -field <b>Edi</b>

<dd>
<p>The destination index register.</p>
</dd>

### -field <b>Ebp</b>

<dd>
<p>The base pointer register.</p>
</dd>

### -field <b>Esp</b>

<dd>
<p>The stack pointer register.</p>
</dd>

### -field <b>Cs</b>

<dd>
<p>The code segment register.</p>
</dd>

### -field <b>Ds</b>

<dd>
<p>The data segment register.</p>
</dd>

### -field <b>Ss</b>

<dd>
<p>The stack segment register.</p>
</dd>

### -field <b>Es</b>

<dd>
<p>The extra segment register.</p>
</dd>

### -field <b>Fs</b>

<dd>
<p>The general purpose segment register FS.</p>
</dd>

### -field <b>Gs</b>

<dd>
<p>The general purpose segment register GS.</p>
</dd>

### -field <b>Eflags</b>

<dd>
<p>The flags register.</p>
</dd>

### -field <b>Eip</b>

<dd>
<p>The instruction pointer register.</p>
</dd>

### -field <b>Cr0</b>

<dd>
<p>The control register 0.</p>
</dd>

### -field <b>Cr1</b>

<dd>
<p>The control register 1.</p>
</dd>

### -field <b>Cr2</b>

<dd>
<p>The control register 2.</p>
</dd>

### -field <b>Cr3</b>

<dd>
<p>The control register 3.</p>
</dd>

### -field <b>Cr4</b>

<dd>
<p>The control register 4.</p>
</dd>

### -field <b>Gdtr</b>

<dd>
<p>The global descriptor table register.</p>
</dd>

### -field <b>Idtr</b>

<dd>
<p>The interrupt descriptor table register.</p>
</dd>

### -field <b>Ldtr</b>

<dd>
<p>The local descriptor table register.</p>
</dd>

### -field <b>Tr</b>

<dd>
<p>The task register.</p>
</dd>
</dl>

## -remarks
<p>If the <b>RegisterContextType</b> member of a <a href="..\ntddk\ns-ntddk--whea-xpf-context-info.md">WHEA_XPF_CONTEXT_INFO</a> structure is set to XPF_CONTEXT_INFO_32BITCONTEXT, the <b>RegisterData</b> member of that structure contains a WHEA_X86_REGISTER_STATE structure.</p>

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
<a href="..\ntddk\ns-ntddk--whea-xpf-context-info.md">WHEA_XPF_CONTEXT_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_X86_REGISTER_STATE structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
