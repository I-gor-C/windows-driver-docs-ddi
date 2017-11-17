---
UID: NC.dispmprt.DXGKDDI_OPM_DESTROY_PROTECTED_OUTPUT
title: DXGKDDI_OPM_DESTROY_PROTECTED_OUTPUT
author: windows-driver-content
description: The DxgkDdiOPMDestroyProtectedOutput function destroys the given protected output object.
old-location: display\dxgkddiopmdestroyprotectedoutput.htm
ms.assetid: a03381ba-342e-409f-99ab-9790e1d74371
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DxgkDdiOPMDestroyProtectedOutput
req.alt-loc: dispmprt.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
ms.keywords: SYMBOL_INFO_EX, SYMBOL_INFO_EX, *PSYMBOL_INFO_EX
req.iface: IDebugSystemObjects4
---

# DXGKDDI_OPM_DESTROY_PROTECTED_OUTPUT callback



## -description
<p>The <i>DxgkDdiOPMDestroyProtectedOutput</i> function destroys the given protected output object.</p>


## -prototype

````
DXGKDDI_OPM_DESTROY_PROTECTED_OUTPUT DxgkDdiOPMDestroyProtectedOutput;

NTSTATUS DxgkDdiOPMDestroyProtectedOutput(
  _In_ PVOID  MiniportDeviceContext,
  _In_ HANDLE ProtectedOutputHandle
)
{ ... }
````


## -parameters
<dl>

### -param <i>MiniportDeviceContext</i> [in]

<dd>
<p>A handle to a context block associated with a display adapter. Previously, the display miniport driver's <a href="https://msdn.microsoft.com/5fd4046f-54c3-4dfc-8d51-0d9ebcde0bea">DxgkDdiAddDevice</a> function provided this handle to the DirectX graphics kernel subsystem.</p>
</dd>

### -param <i>ProtectedOutputHandle</i> [in]

<dd>
<p>The handle to a protected output object. The <a href="https://msdn.microsoft.com/8143732e-cef6-49f1-9b20-db6b6ee073e6">DxgkDdiOPMCreateProtectedOutput</a> function creates the protected output object and returns the handle to the object.</p>
</dd>
</dl>

## -returns
<p><i>DxgkDdiOPMDestroyProtectedOutput</i> returns STATUS_SUCCESS if it succeeds. Otherwise, it returns one of the error codes that are defined in <i>Ntstatus.h</i>. </p>

## -remarks
<p>The DirectX graphics kernel subsystem calls <i>DxgkDdiOPMDestroyProtectedOutput</i> when it finishes using the protected output object.</p>

<p><i>DxgkDdiOPMDestroyProtectedOutput</i> should be made pageable.</p>

<p>The DirectX graphics kernel subsystem calls <i>DxgkDdiOPMDestroyProtectedOutput</i> when it finishes using the protected output object.</p>

<p><i>DxgkDdiOPMDestroyProtectedOutput</i> should be made pageable.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dispmprt.h (include Dispmprt.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL (see Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/5fd4046f-54c3-4dfc-8d51-0d9ebcde0bea">DxgkDdiAddDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/8143732e-cef6-49f1-9b20-db6b6ee073e6">DxgkDdiOPMCreateProtectedOutput</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKDDI_OPM_DESTROY_PROTECTED_OUTPUT callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
