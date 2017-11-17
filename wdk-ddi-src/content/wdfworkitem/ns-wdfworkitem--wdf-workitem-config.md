---
UID: NS.wdfworkitem._WDF_WORKITEM_CONFIG
title: WDF_WORKITEM_CONFIG
author: windows-driver-content
description: The WDF_WORKITEM_CONFIG structure contains information that is associated with a work item.
old-location: wdf\wdf_workitem_config.htm
ms.assetid: b6186c05-ccb9-432c-bd83-9a3fb3af7f0b
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: wdf
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
req.irql: <= DISPATCH_LEVEL
ms.keywords: WDF_WORKITEM_CONFIG, WDF_WORKITEM_CONFIG, *PWDF_WORKITEM_CONFIG
req.iface: 
req.product: Windows 10 or later.
---

# WDF_WORKITEM_CONFIG structure



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_WORKITEM_CONFIG</b> structure contains information that is associated with a work item.</p>


## -syntax

````
typedef struct _WDF_WORKITEM_CONFIG {
  ULONG            Size;
  PFN_WDF_WORKITEM EvtWorkItemFunc;
  BOOLEAN          AutomaticSerialization;
} WDF_WORKITEM_CONFIG, *PWDF_WORKITEM_CONFIG;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this <b>WDF_WORKITEM_CONFIG</b> structure.</p>
</dd>

### -field <b>EvtWorkItemFunc</b>

<dd>
<p>The address of an <a href="https://msdn.microsoft.com/2a2811de-9024-40a8-b8af-b61ca4100218">EvtWorkItem</a> event callback function.</p>
</dd>

### -field <b>AutomaticSerialization</b>

<dd>
<p>A Boolean value that, if <b>TRUE</b>, indicates that the framework will synchronize execution of the <a href="https://msdn.microsoft.com/2a2811de-9024-40a8-b8af-b61ca4100218">EvtWorkItem</a> callback function with callback functions from other objects that are underneath the work-item object's parent object. For more information, see the following Remarks section. If <b>FALSE</b>, the framework does not synchronize execution of the <i>EvtWorkItem</i> callback function.</p>
</dd>
</dl>

## -remarks
<p>Your driver must initialize the <b>WDF_WORKITEM_CONFIG</b> structure by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff553088">WDF_WORKITEM_CONFIG_INIT</a>. Your driver can then pass the structure to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551201">WdfWorkItemCreate</a> method as an input parameter.</p>

<p>Setting the <b>AutomaticSerialization</b> member of <b>WDF_WORKITEM_CONFIG</b> to <b>TRUE</b> has no effect if the parent object's <a href="https://msdn.microsoft.com/a251bf5c-c09b-4097-a9ed-82f2312ac408">synchronization scope</a> is set to <b>WdfSynchronizationScopeNone</b>.</p>

<p>If <b>AutomaticSerialization</b> is <b>TRUE</b>, the parent object's execution level must be <b>WdfExecutionLevelPassive</b>.</p>

<p>For more information about <b>AutomaticSerialization</b> and synchronizing driver callback functions, see <a href="wdf.synchronization_techniques_for_wdf_drivers">Synchronization Techniques for Framework-Based Drivers</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
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
<a href="https://msdn.microsoft.com/2a2811de-9024-40a8-b8af-b61ca4100218">EvtWorkItem</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553088">WDF_WORKITEM_CONFIG_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551201">WdfWorkItemCreate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_WORKITEM_CONFIG structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
