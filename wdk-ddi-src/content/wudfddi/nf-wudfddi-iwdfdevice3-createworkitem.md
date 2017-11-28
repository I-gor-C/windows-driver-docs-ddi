---
UID: NF.wudfddi.IWDFDevice3.CreateWorkItem
title: IWDFDevice3::CreateWorkItem
author: windows-driver-content
description: The CreateWorkItem method creates a framework work-item object, which can subsequently be added to the framework’s work-item queue.
old-location: wdf\iwdfdevice3_createworkitem.htm
old-project: wdf
ms.assetid: B34EABF4-C659-4DB4-AEC6-94F544D79221
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWDFDevice3, CreateWorkItem, IWDFDevice3::CreateWorkItem
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
req.alt-api: IWDFDevice3.CreateWorkItem
req.alt-loc: WUDFx.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: WUDFx.dll
req.irql: <= DISPATCH_LEVEL
req.iface: IWDFDevice3
req.product: Windows 10 or later.
---

# IWDFDevice3::CreateWorkItem method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>CreateWorkItem</b> method creates a framework work-item object, which can subsequently be added to the framework’s work-item queue.</p>


## -syntax

````
HRESULT CreateWorkItem(
  [in]           PWUDF_WORKITEM_CONFIG pConfig,
  [in, optional] IWDFObject            *pParentObject,
  [out]          IWDFWorkItem          **ppWorkItem
);
````


## -parameters
<dl>

### -param <i>pConfig</i> [in]

<dd>
<p>A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/hh464094">WUDF_WORKITEM_CONFIG</a> structure that the driver must have already initialized by calling <a href="https://msdn.microsoft.com/library/windows/hardware/hh464097">WUDF_WORKITEM_CONFIG_INIT</a>.</p>
</dd>

### -param <i>pParentObject</i> [in, optional]

<dd>
<p>A pointer to the parent object interface or NULL.</p>
</dd>

### -param <i>ppWorkItem</i> [out]

<dd>
<p>A pointer to a buffer that receives a pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406734">IWDFWorkItem</a> interface for the new WorkItem object.</p>
</dd>
</dl>

## -returns
<p>The method returns S_OK if the operation succeeds. Otherwise, this method returns one of the error codes that are defined in Winerror.h.</p>

## -remarks
<p>If you specify a parent object, the framework automatically deletes the work-item when the parent object is deleted. Alternatively, the driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff560210">IWDFObject::DeleteWdfObject</a> to delete a work-item. The driver must not delete a work-item in its <a href="..\wudfworkitem\nc-wudfworkitem-wudf-workitem-function.md">OnWorkItem</a> callback function.</p>

<p>For more information, see <a href="wdf.using_workitems">Using Work Items</a>.</p>

<p>If you specify a parent object, the framework automatically deletes the work-item when the parent object is deleted. Alternatively, the driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff560210">IWDFObject::DeleteWdfObject</a> to delete a work-item. The driver must not delete a work-item in its <a href="..\wudfworkitem\nc-wudfworkitem-wudf-workitem-function.md">OnWorkItem</a> callback function.</p>

<p>For more information, see <a href="wdf.using_workitems">Using Work Items</a>.</p>

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
<p>End of support</p>
</th>
<td width="70%">
<p>Unavailable in UMDF 2.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>1.11</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>WUDFx.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451197">IWDFDevice3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406734">IWDFWorkItem</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh464094">WUDF_WORKITEM_CONFIG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh464097">WUDF_WORKITEM_CONFIG_INIT</a>
</dt>
<dt>
<a href="..\wudfworkitem\nc-wudfworkitem-wudf-workitem-function.md">OnWorkItem</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFDevice3::CreateWorkItem method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
