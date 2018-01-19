---
UID : NS:ntddk._WHEA_X64_REGISTER_STATE
title : _WHEA_X64_REGISTER_STATE
author : windows-driver-content
description : The WHEA_X64_REGISTER_STATE structure describes the state of an x64 processor's registers.
old-location : whea\whea_x64_register_state.htm
old-project : whea
ms.assetid : 690c900f-fba8-4712-9a05-bfbe633dd9cf
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : _WHEA_X64_REGISTER_STATE, WHEA_X64_REGISTER_STATE, *PWHEA_X64_REGISTER_STATE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntddk.h
req.include-header : Ntddk.h
req.target-type : Windows
req.target-min-winverclnt : Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : WHEA_X64_REGISTER_STATE
req.alt-loc : ntddk.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : WHEA_X64_REGISTER_STATE, *PWHEA_X64_REGISTER_STATE
---

# _WHEA_X64_REGISTER_STATE structure
The WHEA_X64_REGISTER_STATE structure describes the state of an x64 processor's registers.

## Syntax
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

## Members

        
            `Cr0`

            The control register 0.
        
            `Cr1`

            The control register 1.
        
            `Cr2`

            The control register 2.
        
            `Cr3`

            The control register 3.
        
            `Cr4`

            The control register 4.
        
            `Cr8`

            The control register 8.
        
            `Cs`

            The code segment register.
        
            `Ds`

            The data segment register.
        
            `Eip`

            The instruction pointer register.
        
            `Es`

            The extra segment register.
        
            `Fs`

            The general purpose segment register FS.
        
            `Gdtr`

            A WHEA128A structure that contains the state of the global descriptor table register. The WHEA128A structure describes a 128-bit value and is defined as follows:

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
        
            `Gs`

            The general purpose segment register GS.
        
            `Idtr`

            A WHEA128A structure that contains the state of the interrupt descriptor table register. For a description of the WHEA128A structure, see the description for the <b>Gdtr</b> member.
        
            `Ldtr`

            The local descriptor table register.
        
            `R10`

            The general purpose register R10.
        
            `R11`

            The general purpose register R11.
        
            `R12`

            The general purpose register R12.
        
            `R13`

            The general purpose register R13.
        
            `R14`

            The general purpose register R14.
        
            `R15`

            The general purpose register R15.
        
            `R8`

            The general purpose register R8.
        
            `R9`

            The general purpose register R9.
        
            `Rax`

            The accumulator register.
        
            `Rbp`

            The base pointer register.
        
            `Rbx`

            The base register.
        
            `Rcx`

            The count register.
        
            `Rdi`

            The destination index register.
        
            `Rdx`

            The data register.
        
            `Reserved`

            Reserved for system use.
        
            `Rflags`

            The flags register.
        
            `Rsi`

            The source index register.
        
            `Rsp`

            The stack pointer register.
        
            `Ss`

            The stack segment register.
        
            `Tr`

            The task register.

    ## Remarks
        If the <b>RegisterContextType</b> member of a <a href="..\ntddk\ns-ntddk-_whea_xpf_context_info.md">WHEA_XPF_CONTEXT_INFO</a> structure is set to XPF_CONTEXT_INFO_64BITCONTEXT, the <b>RegisterData</b> member of that structure contains a WHEA_X64_REGISTER_STATE structure.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddk.h (include Ntddk.h) |

    ## See Also

        <dl>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_xpf_context_info.md">WHEA_XPF_CONTEXT_INFO</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_X64_REGISTER_STATE structure%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>