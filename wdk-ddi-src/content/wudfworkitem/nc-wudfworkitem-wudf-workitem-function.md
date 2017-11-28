---
UID: NC.wudfworkitem.WUDF_WORKITEM_FUNCTION
title: WUDF_WORKITEM_FUNCTION
author: windows-driver-content
description: A driver's OnWorkItem event callback function performs the work that is associated with a specified work item.
old-location: wdf\onworkitem.htm
old-project: wdf
ms.assetid: 4CCA1F5E-C92E-4D8D-A8C0-B8E9A0F29703
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: UNICODE_STRING, UNICODE_STRING
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wudfworkitem.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
req.alt-api: WUDF_WORKITEM_FUNCTION
req.alt-loc: Wudfworkitem.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: IWDFUsbTargetPipe2
req.product: Windows 10 or later.
---

# WUDF_WORKITEM_FUNCTION callback



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>A driver's <i>OnWorkItem</i> event callback function performs the work that is associated with a specified work item.</p>


## -prototype

````
WUDF_WORKITEM_FUNCTION OnWorkItem;

void OnWorkItem(
  _In_ IWDFWorkItem *pWorkItem
)
{ ... }

typedef void WUDF_WORKITEM_FUNCTION;
````


## -parameters
<dl>

### -param <i>pWorkItem</i> [in]

<dd>
<p>A pointer to an  <a href="https://msdn.microsoft.com/library/windows/hardware/hh406734">IWDFWorkItem</a> interface.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks
<p>To register an <i>OnWorkItem</i> callback function, your driver must place the callback function's address in a <a href="https://msdn.microsoft.com/library/windows/hardware/hh464094">WUDF_WORKITEM_CONFIG</a> structure before calling <a href="wdf.iwdfdevice3_createworkitem">IWDFDevice3::CreateWorkItem</a>.</p>

<p>Typically, a driver's <i>OnWorkItem</i> callback function performs tasks that are specified by information that the driver stored in the context memory of a work-item object.</p>

<p>The driver must not call <a href="https://msdn.microsoft.com/library/windows/hardware/ff560210">IWDFObject::DeleteWdfObject</a> from the <i>OnWorkItem</i> callback function.</p>

<p>For more information, see <a href="wdf.using_workitems">Using Work Items</a>.</p>

<p>The function type is declared in <i>Wudfworkitem.h</i>, as follows.</p>

<p>To define an <i>OnWorkItem</i> callback function that is named <i>MyWorkItem</i>, you must first provide a function declaration that SDV and other verification tools require, as follows:</p>

<p>Then, implement your callback function as follows:</p>

<p>To register an <i>OnWorkItem</i> callback function, your driver must place the callback function's address in a <a href="https://msdn.microsoft.com/library/windows/hardware/hh464094">WUDF_WORKITEM_CONFIG</a> structure before calling <a href="wdf.iwdfdevice3_createworkitem">IWDFDevice3::CreateWorkItem</a>.</p>

<p>Typically, a driver's <i>OnWorkItem</i> callback function performs tasks that are specified by information that the driver stored in the context memory of a work-item object.</p>

<p>The driver must not call <a href="https://msdn.microsoft.com/library/windows/hardware/ff560210">IWDFObject::DeleteWdfObject</a> from the <i>OnWorkItem</i> callback function.</p>

<p>For more information, see <a href="wdf.using_workitems">Using Work Items</a>.</p>

<p>The function type is declared in <i>Wudfworkitem.h</i>, as follows.</p>

<p>To define an <i>OnWorkItem</i> callback function that is named <i>MyWorkItem</i>, you must first provide a function declaration that SDV and other verification tools require, as follows:</p>

<p>Then, implement your callback function as follows:</p>

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
<dt>Wudfworkitem.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.iwdfdevice3_createworkitem">IWDFDevice3::CreateWorkItem</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh464094">WUDF_WORKITEM_CONFIG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560210">IWDFObject::DeleteWdfObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WUDF_WORKITEM_FUNCTION callback function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
