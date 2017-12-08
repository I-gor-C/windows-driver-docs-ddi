---
UID: NS.WDFWORKITEM._WDF_WORKITEM_CONFIG
title: _WDF_WORKITEM_CONFIG
author: windows-driver-content
description: The WDF_WORKITEM_CONFIG structure contains information that is associated with a work item.
old-location: wdf\wdf_workitem_config.htm
old-project: wdf
ms.assetid: b6186c05-ccb9-432c-bd83-9a3fb3af7f0b
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: _WDF_WORKITEM_CONFIG, WDF_WORKITEM_CONFIG, *PWDF_WORKITEM_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdfworkitem.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_WORKITEM_CONFIG
req.alt-loc: wdfworkitem.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.product: Windows 10 or later.
---

# _WDF_WORKITEM_CONFIG structure



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]
The <b>WDF_WORKITEM_CONFIG</b> structure contains information that is associated with a work item.


## -syntax

````
typedef struct _WDF_WORKITEM_CONFIG {
  ULONG            Size;
  PFN_WDF_WORKITEM EvtWorkItemFunc;
  BOOLEAN          AutomaticSerialization;
} WDF_WORKITEM_CONFIG, *PWDF_WORKITEM_CONFIG;
````


## -struct-fields

### -field Size

The size, in bytes, of this <b>WDF_WORKITEM_CONFIG</b> structure.

### -field EvtWorkItemFunc

The address of an <a href="wdf.evtworkitem">EvtWorkItem</a> event callback function.

### -field AutomaticSerialization

A Boolean value that, if <b>TRUE</b>, indicates that the framework will synchronize execution of the <a href="wdf.evtworkitem">EvtWorkItem</a> callback function with callback functions from other objects that are underneath the work-item object's parent object. For more information, see the following Remarks section. If <b>FALSE</b>, the framework does not synchronize execution of the <i>EvtWorkItem</i> callback function.

## -remarks
Your driver must initialize the <b>WDF_WORKITEM_CONFIG</b> structure by calling <a href="wdf.wdf_workitem_config_init">WDF_WORKITEM_CONFIG_INIT</a>. Your driver can then pass the structure to the <a href="wdf.wdfworkitemcreate">WdfWorkItemCreate</a> method as an input parameter.

Setting the <b>AutomaticSerialization</b> member of <b>WDF_WORKITEM_CONFIG</b> to <b>TRUE</b> has no effect if the parent object's <a href="wdf.wdf_synchronization_scope">synchronization scope</a> is set to <b>WdfSynchronizationScopeNone</b>.

If <b>AutomaticSerialization</b> is <b>TRUE</b>, the parent object's execution level must be <b>WdfExecutionLevelPassive</b>.

For more information about <b>AutomaticSerialization</b> and synchronizing driver callback functions, see <a href="wdf.synchronization_techniques_for_wdf_drivers">Synchronization Techniques for Framework-Based Drivers</a>.

## -requirements
<table>
<tr>
<th width="30%">
Minimum KMDF version
</th>
<td width="70%">
1.0
</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version
</th>
<td width="70%">
2.0
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Wdfworkitem.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.evtworkitem">EvtWorkItem</a>
</dt>
<dt>
<a href="wdf.wdf_workitem_config_init">WDF_WORKITEM_CONFIG_INIT</a>
</dt>
<dt>
<a href="wdf.wdfworkitemcreate">WdfWorkItemCreate</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_WORKITEM_CONFIG structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
