---
UID: NF.wudfddi.IWDFDriver.CreateWdfObject
title: IWDFDriver::CreateWdfObject
author: windows-driver-content
description: The CreateWdfObject method creates a custom (or user) WDF object from a parent WDF object.
old-location: wdf\iwdfdriver_createwdfobject.htm
old-project: wdf
ms.assetid: 9dda353d-7c39-4c3c-b9e2-38946d6cc086
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IWDFDriver, CreateWdfObject, IWDFDriver::CreateWdfObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wudfddi.h
req.include-header: Wudfddi.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.alt-api: IWDFDriver.CreateWdfObject
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
req.iface: IWDFDriver
req.product: Windows 10 or later.
---

# IWDFDriver::CreateWdfObject method



## -description
<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]</p>
<p>The <b>CreateWdfObject</b> method creates a custom (or user) WDF object from a parent WDF object.</p>


## -syntax

````
HRESULT CreateWdfObject(
  [in, optional] IUnknown   *pCallbackInterface,
  [in, optional] IWDFObject *pParentObject,
  [out]          IWDFObject **ppWdfObject
);
````


## -parameters
<dl>

### -param pCallbackInterface [in, optional]

<dd>
<p>A pointer to the <b>IUnknown</b> interface that the framework uses to determine the object-related event callback functions that the driver subscribes to on the newly created custom object. This parameter is optional. The driver can pass <b>NULL</b> if the driver does not require notification. If the driver passes a valid pointer, the framework will call <b>QueryInterface</b> on the <b>IUnknown</b> interface for the <a href="..\wudfddi\nn-wudfddi-iobjectcleanup.md">IObjectCleanup</a> interface. If the framework obtains the driver's <b>IObjectCleanup</b> interface, the framework can subsequently call the driver's <a href="wdf.iobjectcleanup_oncleanup">IObjectCleanup::OnCleanup</a> method to notify the driver that the custom object is cleaned up. </p>
</dd>

### -param pParentObject [in, optional]

<dd>
<p>A pointer to the <a href="..\wudfddi\nn-wudfddi-iwdfobject.md">IWDFObject</a> interface for the parent WDF object. If <b>NULL</b>, the driver object becomes the default parent. </p>
</dd>

### -param ppWdfObject [out]

<dd>
<p>A pointer to a buffer that receives a pointer to the <a href="..\wudfddi\nn-wudfddi-iwdfobject.md">IWDFObject</a> interface for the newly created WDF object.</p>
</dd>
</dl>

## -returns
<p><b>CreateWdfObject</b> returns S_OK if the operation succeeds. Otherwise, this method returns one of the error codes that are defined in Winerror.h.</p>

## -remarks
<p>The driver can call <b>CreateWdfObject</b> to create a general <a href="wdf.framework_base_object">framework base object</a> for its own use. The driver can associate context memory, assign a parent object, and register an <a href="..\wudfddi\nn-wudfddi-iobjectcleanup.md">IObjectCleanup</a> interface. The framework subsequently calls the <a href="wdf.iobjectcleanup_oncleanup">IObjectCleanup::OnCleanup</a> method to clean up the child object. </p>

<p>If no parent object is specified at the <i>pParentObject</i> parameter, the driver becomes the default parent. Therefore, when the driver object is deleted, the framework cleans up the child object. </p>

<p>If a parent object is assigned, the child object is deleted when the parent object is deleted. In other words, the lifetime of a child object is scoped within that of the parent. </p>

<p>If the driver must clean up the child object before the parent object is deleted, the driver can call the <a href="wdf.iwdfobject_deletewdfobject">IWDFObject::DeleteWdfObject</a> method. </p>

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
<p>1.5</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wudfddi.h (include Wudfddi.h)</dt>
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
<a href="..\wudfddi\nn-wudfddi-iwdfdriver.md">IWDFDriver</a>
</dt>
<dt>
<a href="..\wudfddi\nn-wudfddi-iobjectcleanup.md">IObjectCleanup</a>
</dt>
<dt>
<a href="wdf.iobjectcleanup_oncleanup">IObjectCleanup::OnCleanup</a>
</dt>
<dt>
<a href="..\wudfddi\nn-wudfddi-iwdfobject.md">IWDFObject</a>
</dt>
<dt>
<a href="wdf.iwdfobject_deletewdfobject">IWDFObject::DeleteWdfObject</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20IWDFDriver::CreateWdfObject method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
