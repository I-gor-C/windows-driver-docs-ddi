---
UID: NS.ntddk._WHEA_X64_REGISTER_STATE
title: WHEA_X64_REGISTER_STATE
author: windows-driver-content
description: The WHEA_X64_REGISTER_STATE structure describes the state of an x64 processor's registers.
old-location: whea\whea_x64_register_state.htm
old-project: whea
ms.assetid: 690c900f-fba8-4712-9a05-bfbe633dd9cf
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WHEA_X64_REGISTER_STATE, WHEA_X64_REGISTER_STATE, *PWHEA_X64_REGISTER_STATE
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
req.alt-api: WHEA_X64_REGISTER_STATE
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

# WHEA_X64_REGISTER_STATE structure



## -description
<p>The WHEA_X64_REGISTER_STATE structure describes the state of an x64 processor's registers.</p>


## -syntax

````
typedef struct _WHEA_X64_REGISTER_STATE {
  ULONGLONG Rax;
  ULONGLONG Rbx;
  ULONGLONG Rcx;
  ULONGLONG Rdx;
  ULONGLONG Rsi;
  ULONGLONG Rdi;
  ULONGLONG Rbp;
  ULONGLONG Rsp;
  ULONGLONG R8;
  ULONGLONG R9;
  ULONGLONG R10;
  ULONGLONG R11;
  ULONGLONG R12;
  ULONGLONG R13;
  ULONGLONG R14;
  ULONGLONG R15;
  USHORT    Cs;
  USHORT    Ds;
  USHORT    Ss;
  USHORT    Es;
  USHORT    Fs;
  USHORT    Gs;
  ULONG     Reserved;
  ULONGLONG Rflags;
  ULONGLONG Eip;
  ULONGLONG Cr0;
  ULONGLONG Cr1;
  ULONGLONG Cr2;
  ULONGLONG Cr3;
  ULONGLONG Cr4;
  ULONGLONG Cr8;
  WHEA128A  Gdtr;
  WHEA128A  Idtr;
  USHORT    Ldtr;
  USHORT    Tr;
} WHEA_X64_REGISTER_STATE, *PWHEA_X64_REGISTER_STATE;
````


## -struct-fields
<dl>

### -field <b>Rax</b>

<dd>
<p>The accumulator register.</p>
</dd>

### -field <b>Rbx</b>

<dd>
<p>The base register.</p>
</dd>

### -field <b>Rcx</b>

<dd>
<p>The count register.</p>
</dd>

### -field <b>Rdx</b>

<dd>
<p>The data register.</p>
</dd>

### -field <b>Rsi</b>

<dd>
<p>The source index register.</p>
</dd>

### -field <b>Rdi</b>

<dd>
<p>The destination index register.</p>
</dd>

### -field <b>Rbp</b>

<dd>
<p>The base pointer register.</p>
</dd>

### -field <b>Rsp</b>

<dd>
<p>The stack pointer register.</p>
</dd>

### -field <b>R8</b>

<dd>
<p>The general purpose register R8.</p>
</dd>

### -field <b>R9</b>

<dd>
<p>The general purpose register R9.</p>
</dd>

### -field <b>R10</b>

<dd>
<p>The general purpose register R10.</p>
</dd>

### -field <b>R11</b>

<dd>
<p>The general purpose register R11.</p>
</dd>

### -field <b>R12</b>

<dd>
<p>The general purpose register R12.</p>
</dd>

### -field <b>R13</b>

<dd>
<p>The general purpose register R13.</p>
</dd>

### -field <b>R14</b>

<dd>
<p>The general purpose register R14.</p>
</dd>

### -field <b>R15</b>

<dd>
<p>The general purpose register R15.</p>
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

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>Rflags</b>

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

### -field <b>Cr8</b>

<dd>
<p>The control register 8.</p>
</dd>

### -field <b>Gdtr</b>

<dd>
<p>A WHEA128A structure that contains the state of the global descriptor table register. The WHEA128A structure describes a 128-bit value and is defined as follows:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef struct _WHEA128A {
  ULONGLONG  Low;
  LONGLONG  High;
} WHEA128A, *PWHEA128A;</pre>
</td>
</tr>
</table></span></div>
<p></p>
<dl>

### -field <a id="Low"></a><a id="low"></a><a id="LOW"></a><b>Low</b>

<dd>
<p>The low order 64 bits of the 128-bit value.</p>
</dd>

### -field <a id="High"></a><a id="high"></a><a id="HIGH"></a><b>High</b>

<dd>
<p>The high order 64 bits of the 128-bit value.</p>
</dd>
</dl>
</dd>

### -field <b>Idtr</b>

<dd>
<p>A WHEA128A structure that contains the state of the interrupt descriptor table register. For a description of the WHEA128A structure, see the description for the <b>Gdtr</b> member.</p>
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
<p>If the <b>RegisterContextType</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560647">WHEA_XPF_CONTEXT_INFO</a> structure is set to XPF_CONTEXT_INFO_64BITCONTEXT, the <b>RegisterData</b> member of that structure contains a WHEA_X64_REGISTER_STATE structure.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560647">WHEA_XPF_CONTEXT_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_X64_REGISTER_STATE structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
