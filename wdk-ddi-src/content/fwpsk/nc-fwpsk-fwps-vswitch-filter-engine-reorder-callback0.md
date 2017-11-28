---
UID: NC.fwpsk.FWPS_VSWITCH_FILTER_ENGINE_REORDER_CALLBACK0
title: FWPS_VSWITCH_FILTER_ENGINE_REORDER_CALLBACK0
author: windows-driver-content
description: The filter engine calls the vSwitchFilterEngineReorderNotifyRn (FWPS_VSWITCH_FILTER_ENGINE_REORDER_CALLBACK0) callout function to notify the callout driver about events that are associated the virtual switch filter engine reordering.Note  FWPS_VSWITCH_FILTER_ENGINE_REORDER_CALLBACK0 is a specific version of FWPS_VSWITCH_FILTER_ENGINE_REORDER_CALLBACK. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information.
old-location: netvista\fwps_vswitch_filter_engine_reorder_callback0.htm
old-project: netvista
ms.assetid: 2526E8BD-316F-4B8D-9CC4-66F4E3B7D708
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: FwpmEngineOpen0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: vSwitchFilterEngineReorderNotifyRn
req.alt-loc: fwpsk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# FWPS_VSWITCH_FILTER_ENGINE_REORDER_CALLBACK0 callback



## -description
<p>The filter engine calls the  
  
  <i>vSwitchFilterEngineReorderNotifyRn</i> (<i>FWPS_VSWITCH_FILTER_ENGINE_REORDER_CALLBACK0</i>) callout function to notify the callout driver about events that are
  associated the virtual switch  filter engine reordering.<div class="alert"><b>Note</b>  <i>FWPS_VSWITCH_FILTER_ENGINE_REORDER_CALLBACK0</i> is a specific version of <i>FWPS_VSWITCH_FILTER_ENGINE_REORDER_CALLBACK</i>. See <a href="fwp.wfp_version-independent_names_and_targeting_specific_versions_of_windows">WFP Version-Independent Names and Targeting Specific Versions of Windows</a> for more information.</div>
<div> </div>
</p>


## -prototype

````
FWPS_VSWITCH_FILTER_ENGINE_REORDER_CALLBACK0 vSwitchFilterEngineReorderNotifyRn;

NTSTATUS NTAPI vSwitchFilterEngineReorderNotifyRn(
  _In_opt_       void              *notifyContext,
  _In_           void              *completionContext,
  _In_           BOOLEAN           isInRequiredPosition,
  _In_     const NDIS_ENUM_FILTERS *vSwitchExtensionLwfList
)
{ ... }
````


## -parameters
<dl>

### -param <i>notifyContext</i> [in, optional]

<dd>
<p>A pointer to a context provided by the callout driver. The driver passed this pointer to the <i>notifyContext</i> parameter of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439687">FwpsvSwitchEventsSubscribe0</a>
 function. This parameter is optional and can be NULL.</p>
</dd>

### -param <i>completionContext</i> [in]

<dd>
<p>A pointer to a completion context provided by the callout driver. This parameter is optional and can be NULL.

</p>
</dd>

### -param <i>isInRequiredPosition</i> [in]

<dd>
<p>A BOOLEAN value that is set to TRUE if the filter is in the required position in the filter stack or FALSE if it is not.</p>
</dd>

### -param <i>vSwitchExtensionLwfList</i> [in]

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/ff565457">NDIS_ENUM_FILTERS</a> structure that specifies a list of the virtual switch extension NDIS filter drivers.</p>
</dd>
</dl>

## -returns
<p>A callout's 
  
  <i>FWPS_VSWITCH_FILTER_ENGINE_REORDER_CALLBACK0</i> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The callout driver accepts the notification from the filter engine.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred. </p>

<p> </p>

## -remarks
<p>A callout driver registers a 
  
  <i>vSwitchFilterEngineReorderNotifyRn</i> function  by calling  
    
    the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439687">FwpsvSwitchEventsSubscribe0</a>
 function.</p>

<p>By default, the WFP virtual switch extension is positioned as the first filtering extension at virtual switch ingress. (Therefore, it is also the last extension at virtual switch egress). This is usually the best position, because the WFP extension can intercept packets before any other extensions can modify them at ingress. Also, the WFP extension can intercept packets after all packet modifications are done at egress.</p>

<p>

However, because an administrator can reorder any virtual switch extensions of the same class, the WFP extension can be reordered out of the default position. After a reorder occurs, a WFP client’s filters could be bypassed and might need to be adjusted.</p>

<p>If the <i>vSwitchFilterEngineReorderNotifyRn</i> callback is registered, the callout driver is notified when a virtual switch reorder is occurring. The callout driver receives an <a href="https://msdn.microsoft.com/library/windows/hardware/ff565457">NDIS_ENUM_FILTERS</a> structure with an ordered list of current virtual switch extensions in the <i>vSwitchExtensionLwfList</i> parameter.</p>

<p>If the virtual switch extensions are reordered, the WFP extension is  paused (see <a href="..\ndis\nc-ndis-filter-pause.md">FilterPause</a>) and restarted (see <a href="..\ndis\nc-ndis-filter-restart.md">FilterRestart</a>). From the WFP filter <i>FilterRestart</i> call, the WFP filter driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561758">NdisEnumerateFilterModules</a> function to obtain an ordered list of virtual switch extension filters.  If the WFP extension is not in the default position, then the filter driver notifies the callout drivers.</p>

<p>A callout driver cannot return STATUS_PENDING from <i>vSwitchFilterEngineReorderNotifyRn</i>.</p>

<p>A callout driver registers a 
  
  <i>vSwitchFilterEngineReorderNotifyRn</i> function  by calling  
    
    the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439687">FwpsvSwitchEventsSubscribe0</a>
 function.</p>

<p>By default, the WFP virtual switch extension is positioned as the first filtering extension at virtual switch ingress. (Therefore, it is also the last extension at virtual switch egress). This is usually the best position, because the WFP extension can intercept packets before any other extensions can modify them at ingress. Also, the WFP extension can intercept packets after all packet modifications are done at egress.</p>

<p>

However, because an administrator can reorder any virtual switch extensions of the same class, the WFP extension can be reordered out of the default position. After a reorder occurs, a WFP client’s filters could be bypassed and might need to be adjusted.</p>

<p>If the <i>vSwitchFilterEngineReorderNotifyRn</i> callback is registered, the callout driver is notified when a virtual switch reorder is occurring. The callout driver receives an <a href="https://msdn.microsoft.com/library/windows/hardware/ff565457">NDIS_ENUM_FILTERS</a> structure with an ordered list of current virtual switch extensions in the <i>vSwitchExtensionLwfList</i> parameter.</p>

<p>If the virtual switch extensions are reordered, the WFP extension is  paused (see <a href="..\ndis\nc-ndis-filter-pause.md">FilterPause</a>) and restarted (see <a href="..\ndis\nc-ndis-filter-restart.md">FilterRestart</a>). From the WFP filter <i>FilterRestart</i> call, the WFP filter driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561758">NdisEnumerateFilterModules</a> function to obtain an ordered list of virtual switch extension filters.  If the WFP extension is not in the default position, then the filter driver notifies the callout drivers.</p>

<p>A callout driver cannot return STATUS_PENDING from <i>vSwitchFilterEngineReorderNotifyRn</i>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fwpsk.h (include Fwpsk.h)</dt>
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
<dt>
<a href="..\ndis\nc-ndis-filter-pause.md">FilterPause</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-filter-restart.md">FilterRestart</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439687">FwpsvSwitchEventsSubscribe0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439695">FwpsvSwitchNotifyComplete0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565457">NDIS_ENUM_FILTERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561758">NdisEnumerateFilterModules</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562610">NdisFRestartComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543875">Callout Driver Callout Functions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FWPS_VSWITCH_FILTER_ENGINE_REORDER_CALLBACK0 callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
