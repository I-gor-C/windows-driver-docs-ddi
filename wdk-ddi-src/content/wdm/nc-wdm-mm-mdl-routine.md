---
UID: NC.wdm.MM_MDL_ROUTINE
title: MM_MDL_ROUTINE
author: windows-driver-content
description: A driver-supplied callback routine that is invoked after a memory descriptor list (MDL) is mapped by calling the MmMapMdl function.
old-location: kernel\mm_mdl_routine.htm
old-project: kernel
ms.assetid: D8D946C9-8642-4D31-B983-DAF88B46B97B
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdm.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: *PMM_MDL_ROUTINE
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# MM_MDL_ROUTINE callback



## -description
<p>A driver-supplied callback routine that is invoked after a memory descriptor
    list (MDL)  is mapped by calling the <a href="..\wdm\nf-wdm-mmmapmdl.md">MmMapMdl</a> function.</p>


## -prototype

````
MM_MDL_ROUTINE MmMdlRoutine;

VOID MmMdlRoutine(
  _In_opt_ PVOID DriverContext,
  _In_     PVOID MappedVa
)
{ ... }

typedef MM_MDL_ROUTINE *PMM_MDL_ROUTINE;
````


## -parameters
<dl>

### -param <i>DriverContext</i> [in, optional]

<dd>
<p>A pointer to a driver-defined context. The driver's callback function can store any status information  in the driver context and then examine the value, when the callback is invoked. </p>
</dd>

### -param <i>MappedVa</i> [in]

<dd>
<p>A pointer to a buffer that contains the system virtual address of the
        mapping.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1709</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-mmmapmdl.md">MmMapMdl</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20MM_MDL_ROUTINE callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
