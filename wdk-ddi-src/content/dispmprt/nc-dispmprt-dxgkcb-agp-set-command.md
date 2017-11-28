---
UID: NC.dispmprt.DXGKCB_AGP_SET_COMMAND
title: DXGKCB_AGP_SET_COMMAND
author: windows-driver-content
description: The AgpSetCommand function sets the AGP rate and specifies whether side band addressing and fast write transactions are enabled.
old-location: display\agpsetcommand.htm
old-project: display
ms.assetid: 4440bc0f-01cb-4108-bfe8-9d5127777f00
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: SYMBOL_INFO_EX, SYMBOL_INFO_EX, *PSYMBOL_INFO_EX
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AgpSetCommand
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
req.irql: PASSIVE_LEVEL
req.iface: IDebugSystemObjects4
---

# DXGKCB_AGP_SET_COMMAND callback



## -description
<p>The <b>AgpSetCommand</b> function sets the AGP rate and specifies whether side band addressing and fast write transactions are enabled.</p>


## -prototype

````
DXGKCB_AGP_SET_COMMAND AgpSetCommand;

NTSTATUS APIENTRY AgpSetCommand(
  _In_ HANDLE Context,
  _In_ ULONG  Command
)
{ ... }
````


## -parameters
<dl>

### -param <i>Context</i> [in]

<dd>
<p>A handle to a context block that is associated with an AGP interface. The display miniport driver previously received this handle in the <b>Context</b> member of the DXGK_AGP_INTERFACE structure that was filled in by <a href="..\dispmprt\nc-dispmprt-dxgkcb-query-services.md">DxgkCbQueryServices</a>.</p>
</dd>

### -param <i>Command</i> [in]

<dd>
<p>A set of flags that specify the AGP rate and the types of AGP transactions that will be used.</p>
<p>The caller must set one, and only one, of the following flags.</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>DXGK_AGPCOMMAND_AGP1X</p>
</td>
<td>
<p>The AGP transfer rate is 1X.</p>
</td>
</tr>
<tr>
<td>
<p>DXGK_AGPCOMMAND_AGP2X</p>
</td>
<td>
<p>The AGP transfer rate is 2X.</p>
</td>
</tr>
<tr>
<td>
<p>DXGK_AGPCOMMAND_AGP4X</p>
</td>
<td>
<p>The AGP transfer rate is 4X.</p>
</td>
</tr>
<tr>
<td>
<p>DXGK_AGPCOMMAND_AGP8X</p>
</td>
<td>
<p>The AGP transfer rate is 8X.</p>
</td>
</tr>
</table>
<p> </p>
<p>The caller might also choose to set or clear the following flags.</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>DXGK_AGPCOMMAND_DISABLE_SBA</p>
</td>
<td>
<p>If this flag is set, side band addressing is disabled. If this flag is cleared, side band addressing is enabled.</p>
</td>
</tr>
<tr>
<td>
<p>DXGK_AGPCOMMAND_DISABLE_FW</p>
</td>
<td>
<p>If this flag is set, fast write transactions are disabled. If this flag is cleared, fast write transactions are enabled. Note that fast write transactions cannot be used with AGP1X.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p><b>AgpSetCommand</b> returns STATUS_SUCCESS if it succeeds. Otherwise, it returns one of the error codes defined in <i>Ntstatus.h</i>.</p>

## -remarks
<p>None.</p>

<p>None.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\dispmprt\nc-dispmprt-dxgkcb-agp-allocate-pool.md">AgpAllocatePool</a>
</dt>
<dt>
<a href="..\dispmprt\nc-dispmprt-dxgkcb-agp-free-pool.md">AgpFreePool</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560949">DXGK_AGP_INTERFACE</a>
</dt>
<dt>
<a href="..\dispmprt\nc-dispmprt-dxgkcb-query-services.md">DxgkCbQueryServices</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKCB_AGP_SET_COMMAND callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
