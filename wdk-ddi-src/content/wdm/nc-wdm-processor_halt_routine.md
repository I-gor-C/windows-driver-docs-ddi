---
UID: NC.wdm.PROCESSOR_HALT_ROUTINE
title: PROCESSOR_HALT_ROUTINE
author: windows-driver-content
description: A Halt callback routine transitions the processor to an idle state.
old-location: kernel\halt.htm
old-project: kernel
ms.assetid: 425239C1-4FBE-4703-B7DB-9DCC17562A6C
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, PWDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdm.h
req.include-header: Pepfx.h
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: Halt
req.alt-loc: wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks.
req.product: Windows 10 or later.
---

# PROCESSOR_HALT_ROUTINE callback



## -description
A <i>Halt</i> callback routine transitions the processor to an idle state.



## -prototype

````
PROCESSOR_HALT_ROUTINE Halt;

NTSTATUS Halt(
  _Inout_opt_ PVOID Context
)
{ ... }
````


## -parameters

### -param Context [in, out, optional]

A pointer to a PEP-defined processor-halt context. This pointer is the <i>Context</i> parameter value that the PEP previously passed to the <a href="..\pepfx\nc-pepfx-pofxcallbackprocessorhalt.md">ProcessorHalt</a> routine.


## -returns
A <i>Halt</i> callback routine may or may not return. If this routine does return, it returns STATUS_SUCCESS to indicates that the processor successfully entered the idle state. Otherwise, it returns an appropriate error status code.


## -remarks
This routine is implemented by the platform extension plug-in (PEP) and is called by the Windows <a href="kernel.power_management_framework__pofx__routines">power management framework</a> (PoFx). The <a href="..\pepfx\nc-pepfx-pofxcallbackprocessorhalt.md">ProcessorHalt</a> routine accepts a pointer to a <i>Halt</i> callback routine as a parameter.

The PEP's <i>Halt</i> routine is called at the same IRQL at which the PEP called <b>ProcessorHalt</b>.


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Supported starting with Windows 10.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Pepfx.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
See Remarks.

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.pep_crashdump_information">PEP_CRASHDUMP_INFORMATION</a>
</dt>
<dt>
<a href="..\pepfx\nc-pepfx-pofxcallbackprocessorhalt.md">ProcessorHalt</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PROCESSOR_HALT_ROUTINE routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

