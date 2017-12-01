---
UID: NF.ndis.NdisFGetOptionalSwitchHandlers
title: NdisFGetOptionalSwitchHandlers
author: windows-driver-content
description: Hyper-V extensible switch extensions call the NdisFGetOptionalSwitchHandlers function to obtain a list of pointers to the Hyper-V extensible switch handler functions.
old-location: netvista\ndisfgetoptionalswitchhandlers.htm
old-project: netvista
ms.assetid: bf034ecd-5c1b-4117-a7b0-bcca3971386b
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisFGetOptionalSwitchHandlers
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisFGetOptionalSwitchHandlers
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# NdisFGetOptionalSwitchHandlers function



## -description
<p>
<p>Hyper-V extensible switch extensions call the <b>NdisFGetOptionalSwitchHandlers</b> function to obtain a list of pointers to the Hyper-V extensible switch handler functions.

</p>
</p>
<p>Hyper-V extensible switch extensions call the <b>NdisFGetOptionalSwitchHandlers</b> function to obtain a list of pointers to the Hyper-V extensible switch handler functions.

</p>


## -syntax

````
NDIS_STATUS NdisFGetOptionalSwitchHandlers(
  _In_    NDIS_HANDLE                    NdisFilterHandle,
  _Out_   PNDIS_SWITCH_CONTEXT           NdisSwitchContext,
  _Inout_ PNDIS_SWITCH_OPTIONAL_HANDLERS NdisSwitchHandlers
);
````


## -parameters
<dl>

### -param <i>NdisFilterHandle</i> [in]

<dd>
<p>The NDIS handle that identifies this filter module. When NDIS called the extension's  <a href="..\ndis\nc-ndis-filter-attach.md">FilterAttach</a> function, it passed this handle in the <i>NdisFilterHandle</i> parameter.</p>
</dd>

### -param <i>NdisSwitchContext</i> [out]

<dd>
<p>A pointer to the NDIS_SWITCH_CONTEXT value that identifies the extensible switch module to which the extension is attached. When  the  extension calls an extensible switch  handler  function, it must set the     <i>NdisSwitchContext</i> parameter to the value of this handle.</p>
</dd>

### -param <i>NdisSwitchHandlers</i> [in, out]

<dd>
<p>A pointer to a caller-allocated  <a href="..\ndis\ns-ndis--ndis-switch-optional-handlers.md">NDIS_SWITCH_OPTIONAL_HANDLERS</a> structure. If the call succeeds, this structure will contain a list of pointers to the extensible switch handler functions.</p>
<p>For more information about these handler functions, see <a href="netvista.hyper_v_extensible_switch_handler_functions">Hyper-V Extensible Switch Handler Functions</a>.</p>
<div class="alert"><b>Note</b>  Before the extension calls <b>NdisFGetOptionalSwitchHandlers</b>, it must initialize the <b>Header</b> member of the <a href="..\ndis\ns-ndis--ndis-switch-optional-handlers.md">NDIS_SWITCH_OPTIONAL_HANDLERS</a> structure.</div>
<div> </div>
</dd>
</dl>

## -returns
<p>If the call succeeds, <b>NdisFGetOptionalSwitchHandlers</b> returns NDIS_STATUS_SUCCESS. Otherwise, it returns NDIS_STATUS_NOT_SUPPORTED if the extensible switch extension is not bound to the underlying extensible switch component.

</p>

## -remarks
<p>The  extension calls the <b>NdisFGetOptionalSwitchHandlers</b> function from its <a href="..\ndis\nc-ndis-filter-attach.md">FilterAttach</a> function. </p>

<p>If the extension is installed with multiple <b>FilterMediaTypes</b> INF entries, the call to <b>NdisFGetOptionalSwitchHandlers</b> lets the extension  determine whether it is bound and attached to the driver stack for either the extensible switch or a physical network adapter. If the call returns NDIS_STATUS_SUCCESS, the extension is attached within the extensible switch driver stack. If the call returns NDIS_STATUS_NOT_SUPPORTED, the extension is attached within the driver stack for a physical network adapter.</p>

<p>For more information about <b>FilterMediaTypes</b> INF entries for extensible switch extensions, see <a href="NULL">INF Requirements for Hyper-V Extensible Switch Extensions</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.30 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><b></b></dt>
<dt>
<a href="..\ndis\nc-ndis-filter-attach.md">FilterAttach</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--ndis-switch-optional-handlers.md">NDIS_SWITCH_OPTIONAL_HANDLERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisFGetOptionalSwitchHandlers function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
