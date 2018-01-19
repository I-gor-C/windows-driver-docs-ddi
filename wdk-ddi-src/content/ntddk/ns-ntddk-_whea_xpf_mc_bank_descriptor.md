---
UID : NS:ntddk._WHEA_XPF_MC_BANK_DESCRIPTOR
title : _WHEA_XPF_MC_BANK_DESCRIPTOR
author : windows-driver-content
description : The WHEA_XPF_MC_BANK_DESCRIPTOR structure describes a bank of machine check registers for an x86 or x64 processor.
old-location : whea\whea_xpf_mc_bank_descriptor.htm
old-project : whea
ms.assetid : e5360f75-53cf-4025-9a1c-665c098329dd
ms.author : windowsdriverdev
ms.date : 12/14/2017
ms.keywords : _WHEA_XPF_MC_BANK_DESCRIPTOR, WHEA_XPF_MC_BANK_DESCRIPTOR, *PWHEA_XPF_MC_BANK_DESCRIPTOR
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
req.alt-api : WHEA_XPF_MC_BANK_DESCRIPTOR
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
req.typenames : WHEA_XPF_MC_BANK_DESCRIPTOR, *PWHEA_XPF_MC_BANK_DESCRIPTOR
---

# _WHEA_XPF_MC_BANK_DESCRIPTOR structure
The WHEA_XPF_MC_BANK_DESCRIPTOR structure describes a bank of machine check registers for an x86 or x64 processor.

## Syntax
````
typedef struct _WHEA_XPF_MC_BANK_DESCRIPTOR {
  UCHAR             BankNumber;
  BOOLEAN           ClearOnInitialization;
  UCHAR             StatusDataFormat;
  XPF_MC_BANK_FLAGS Flags;
  ULONG             ControlMsr;
  ULONG             StatusMsr;
  ULONG             AddressMsr;
  ULONG             MiscMsr;
  ULONGLONG         ControlData;
} WHEA_XPF_MC_BANK_DESCRIPTOR, *PWHEA_XPF_MC_BANK_DESCRIPTOR;
````

## Members

        
            `AddressMsr`

            The model-specific register address of the register bank's IA32_MCi_ADDR register. For more information about the IA32_MCi_ADDR register, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=78804">Intel 64 and IA-32 Architectures Software Developer's Manual</a>.
        
            `BankNumber`

            The processor machine check register bank number.
        
            `ClearOnInitialization`

            A Boolean value that indicates that the status registers for the bank are to be cleared by the operating system during initialization.
        
            `ControlData`

            The value that the operating system writes to the register bank's control register during initialization.
        
            `ControlMsr`

            The model-specific register address of the register bank's IA32_MCi_CTL register. For more information about the IA32_MCi_CTL register, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=78804">Intel 64 and IA-32 Architectures Software Developer's Manual</a>.
        
            `Flags`

            An XPF_MC_BANK_FLAGS union that indicates which of the members of the WHEA_XPF_MC_BANK_DESCRIPTOR structure can be written to by the operating system. The XPF_MC_BANK_FLAGS union is defined as follows:

<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef union _XPF_MC_BANK_FLAGS {
  struct {
    UCHAR  ClearOnInitializationRW:1;
    UCHAR  ControlDataRW:1;
    UCHAR  Reserved:6;
  };
  UCHAR  AsUCHAR;
} XPF_MC_BANK_FLAGS, *PXPF_MC_BANK_FLAGS;</pre>
</td>
</tr>
</table></span></div>
        
            `MiscMsr`

            The model-specific register address of the register bank's IA32_MCi_MISC register. For more information about the IA32_MCi_MISC register, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=78804">Intel 64 and IA-32 Architectures Software Developer's Manual</a>.
        
            `StatusDataFormat`

            The format of the data in the register bank's status register. Possible values are:
        
            `StatusMsr`

            The model-specific register address of the register bank's IA32_MCi_STATUS register. For more information about the IA32_MCi_STATUS register, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=78804">Intel 64 and IA-32 Architectures Software Developer's Manual</a>.

    ## Remarks
        An array of WHEA_XPF_MC_BANK_DESCRIPTOR structures is contained in the <a href="..\ntddk\ns-ntddk-_whea_xpf_cmc_descriptor.md">WHEA_XPF_CMC_DESCRIPTOR</a> and <a href="..\ntddk\ns-ntddk-_whea_xpf_mce_descriptor.md">WHEA_XPF_MCE_DESCRIPTOR</a> structures.

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
<a href="..\ntddk\ns-ntddk-_whea_xpf_cmc_descriptor.md">WHEA_XPF_CMC_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk-_whea_xpf_mce_descriptor.md">WHEA_XPF_MCE_DESCRIPTOR</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_XPF_MC_BANK_DESCRIPTOR structure%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>