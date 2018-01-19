---
UID : NN:wudfddi.IObjectCleanup
title : IObjectCleanup
author : windows-driver-content
description : Any driver that stores a reference-counted COM interface to a WDF object must support the IObjectCleanup interface to prevent interface leakage. Note that drivers, in general, are not required to hold references to WDF objects.
old-location : wdf\iobjectcleanup.htm
old-project : wdf
ms.assetid : 5e465c90-3290-4c89-bf47-521280c0fe5c
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : IWDFWorkItem, IWDFWorkItem::GetParentObject, GetParentObject
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : wudfddi.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IObjectCleanup
req.alt-loc : Wudfddi.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : WUDFx.dll
req.irql : 
req.typenames : "*PPOWER_ACTION, POWER_ACTION"
req.product : Windows 10 or later.
---

# IObjectCleanup interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

Any driver that stores a reference-counted COM interface to a WDF object must support the <b>IObjectCleanup</b> interface to prevent interface leakage. Note that drivers, in general, are not required to hold references to WDF objects.

## Methods

<p>The <b>IObjectCleanup</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfddi.IObjectCleanup.OnCleanup](nf-wudfddi-iobjectcleanup-oncleanup.md) | The OnCleanup method releases any references to a WDF object to prevent interface leakage. |

## Remarks

The framework calls the method of the <b>IObjectCleanup</b> interface when the associated framework object is about to be released.

A driver can register the <b>IObjectCleanup</b> interface when the driver calls any method that creates a WDF object. </p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | wudfddi.h |
| **DLL** | WUDFx.dll |