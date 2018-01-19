---
UID : NN:wudfddi.IWDFObject
title : IWDFObject
author : windows-driver-content
description : The IWDFObject interface exposes the framework base object that provides the basic functionality common across all framework object types. All framework objects are derived from this root object.
old-location : wdf\iwdfobject.htm
old-project : wdf
ms.assetid : d2668856-a25d-4329-b230-f36992f8f9a4
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : IWDFWorkItem, IWDFWorkItem::GetParentObject, GetParentObject
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : wudfddi.h
req.include-header : 
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 1.5
req.alt-api : IWDFObject
req.alt-loc : WUDFx.dll
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : Unavailable in UMDF 2.0 and later.
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : WUDFx.dll
req.irql : 
req.typenames : "*PPOWER_ACTION, POWER_ACTION"
req.product : Windows 10 or later.
---

# IWDFObject interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IWDFObject</b> interface exposes the framework base object that provides the basic functionality common across all framework object types. All framework objects are derived from this root object.

## Methods

<p>The <b>IWDFObject</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfddi.IWDFObject.AcquireLock](nf-wudfddi-iwdfobject-acquirelock.md) | The AcquireLock method prevents the framework from calling methods of interfaces that a driver registered. |
| [wudfddi.IWDFObject.AssignContext](nf-wudfddi-iwdfobject-assigncontext.md) | The AssignContext method registers a context and a driver-supplied cleanup callback function for the object. |
| [wudfddi.IWDFObject.DeleteWdfObject](nf-wudfddi-iwdfobject-deletewdfobject.md) | The DeleteWdfObject method deletes a previously created Microsoft Windows Driver Frameworks (WDF) object. |
| [wudfddi.IWDFObject.ReleaseLock](nf-wudfddi-iwdfobject-releaselock.md) | The ReleaseLock method allows the framework to call methods of interfaces that are registered by the driver that the framework previously prevented from calling because the driver called the IWDFObject::AcquireLock method. |
| [wudfddi.IWDFObject.RetrieveContext](nf-wudfddi-iwdfobject-retrievecontext.md) | The RetrieveContext method retrieves a context that was previously registered through the IWDFObject::AssignContext method. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum UMDF version** | 1.5 |
| **Header** | wudfddi.h |
| **DLL** | WUDFx.dll |