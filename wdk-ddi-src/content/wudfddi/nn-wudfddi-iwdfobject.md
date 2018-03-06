---
UID: NN:wudfddi.IWDFObject
title: IWDFObject
author: windows-driver-content
description: The IWDFObject interface exposes the framework base object that provides the basic functionality common across all framework object types. All framework objects are derived from this root object.
old-location: wdf\iwdfobject.htm
old-project: wdf
ms.assetid: d2668856-a25d-4329-b230-f36992f8f9a4
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IWDFObject, IWDFObject interface, IWDFObject interface, described, UMDFBaseObjectRef_b2026a30-0f91-4793-8622-093ca142f794.xml, umdf.iwdfobject, wdf.iwdfobject, wudfddi/IWDFObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.5
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: Unavailable in UMDF 2.0 and later.
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: wudfddi.h
req.dll: WUDFx.dll
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	WUDFx.dll
api_name:
-	IWDFObject
product: Windows
targetos: Windows
req.typenames: POWER_ACTION, *PPOWER_ACTION
req.product: Windows 10 or later.
---

# IWDFObject interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IWDFObject</b> interface exposes the framework base object that provides the basic functionality common across all framework object types. All framework objects are derived from this root object.

## Methods

<p>The <b>IWDFObject</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDFObject::AcquireLock](nf-wudfddi-iwdfobject-acquirelock.md) | The AcquireLock method prevents the framework from calling methods of interfaces that a driver registered. |
| [IWDFObject::AssignContext](nf-wudfddi-iwdfobject-assigncontext.md) | The AssignContext method registers a context and a driver-supplied cleanup callback function for the object. |
| [IWDFObject::DeleteWdfObject](nf-wudfddi-iwdfobject-deletewdfobject.md) | The DeleteWdfObject method deletes a previously created Microsoft Windows Driver Frameworks (WDF) object. |
| [IWDFObject::ReleaseLock](nf-wudfddi-iwdfobject-releaselock.md) | The ReleaseLock method allows the framework to call methods of interfaces that are registered by the driver that the framework previously prevented from calling because the driver called the IWDFObject::AcquireLock method. |
| [IWDFObject::RetrieveContext](nf-wudfddi-iwdfobject-retrievecontext.md) | The RetrieveContext method retrieves a context that was previously registered through the IWDFObject::AssignContext method. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **End of support** | Unavailable in UMDF 2.0 and later.  |
| **Target Platform** | Desktop |
| **Minimum UMDF version** | 1.5 |
| **Header** | wudfddi.h |