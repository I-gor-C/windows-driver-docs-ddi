---
UID: NF.wudfddi.IWDFObject.AssignContext
title: IWDFObject::AssignContext method
author: windows-driver-content
description: The AssignContext method registers a context and a driver-supplied cleanup callback function for the object.
old-location: wdf\iwdfobject_assigncontext.htm
old-project: wdf
ms.assetid: 9b543d5d-ed6d-4440-b5ad-aefca69dd489
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: IWDFObject, IWDFObject::AssignContext, AssignContext
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFObject.AssignContext
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
req.irql: 
req.product: Windows 10 or later.
---

# IWDFObject::AssignContext method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>AssignContext</b> method registers a context and a driver-supplied cleanup callback function for the object.



## -syntax

````
HRESULT AssignContext(
  [in, optional] IObjectCleanup *pCleanupCallback,
  [in, optional] void           *pContext
);
````


## -parameters

### -param pCleanupCallback [in, optional]

A pointer to the <a href="..\wudfddi\nn-wudfddi-iobjectcleanup.md">IObjectCleanup</a> interface that contains the cleanup callback function, which performs cleanup operations for the object if it becomes invalid. This parameter is optional. The driver can pass <b>NULL</b> if the driver does not require notification when the object is cleaned up. 


### -param pContext [in, optional]

A pointer to the context to register. <b>NULL</b> is a valid context. 


## -returns
<b>AssignContext</b> returns S_OK if the operation succeeds. Otherwise, this method returns one of the error codes that are defined in Winerror.h.


## -remarks
A driver calls <b>AssignContext</b> to register a context and to request notification when the object becomes invalid. In a <b>AssignContext</b> call, the driver passes a pointer to the <a href="..\wudfddi\nn-wudfddi-iobjectcleanup.md">IObjectCleanup</a> interface in the <i>pCleanupCallback</i> parameter to register <b>IObjectCleanup</b>. Note that the framework internally holds a reference to the supplied <b>IObjectCleanup</b> interface while the object is valid. When the object becomes invalid, the framework calls the <a href="wdf.iobjectcleanup_oncleanup">IObjectCleanup::OnCleanup</a> method to notify the driver. The framework automatically releases the reference to the supplied <b>IObjectCleanup</b> after calling <b>IObjectCleanup::OnCleanup</b>.

At any given time, only one context that is associated with each object instance can exist. Attempts to register additional contexts fail.

A context can be associated only with an object that is in a valid state. For example, an attempt to associate a context with an object that is in the process of deletion fails.

Because the context is not a Component Object Model (COM) interface, the driver must not treat the context as such. For example, the driver cannot call the <b>AddRef</b> method on the context.

The <a href="wdf.iwdfobject_retrievecontext">IWDFObject::RetrieveContext</a> method can be used to retrieve the context that was previously registered through <b>AssignContext</b>.

For a code example of how to use the <b>AssignContext</b> method, see <a href="wdf.iwdfiotarget_formatrequestforwrite">IWDFIoTarget::FormatRequestForWrite</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
End of support

</th>
<td width="70%">
Unavailable in UMDF 2.0 and later.

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
1.5

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

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
<a href="..\wudfddi\nn-wudfddi-iwdfobject.md">IWDFObject</a>
</dt>
<dt>
<a href="..\wudfddi\nn-wudfddi-iobjectcleanup.md">IObjectCleanup</a>
</dt>
<dt>
<a href="wdf.iobjectcleanup_oncleanup">IObjectCleanup::OnCleanup</a>
</dt>
<dt>
<a href="wdf.iwdfobject_retrievecontext">IWDFObject::RetrieveContext</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFObject::AssignContext method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

