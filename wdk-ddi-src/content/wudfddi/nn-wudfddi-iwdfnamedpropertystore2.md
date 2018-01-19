---
UID : NN:wudfddi.IWDFNamedPropertyStore2
title : IWDFNamedPropertyStore2
author : windows-driver-content
description : Drivers obtain the IWDFNamedPropertyStore2 interface by calling IWDFPropertyStoreFactory::RetrieveDevicePropertyStore.
old-location : wdf\iwdfnamedpropertystore2.htm
old-project : wdf
ms.assetid : f6935379-bf0d-4319-bcd9-56f0e4016945
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
req.umdf-ver : 1.9
req.alt-api : IWDFNamedPropertyStore2
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

# IWDFNamedPropertyStore2 interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

Drivers obtain the <b>IWDFNamedPropertyStore2</b> interface by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff560228">IWDFPropertyStoreFactory::RetrieveDevicePropertyStore</a>.

## Methods

<p>The <b>IWDFNamedPropertyStore2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfddi.IWDFNamedPropertyStore2.DeleteNamedValue](nf-wudfddi-iwdfnamedpropertystore2-deletenamedvalue.md) | The DeleteNamedValue method deletes a value name from the registry. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum UMDF version** | 1.9 |
| **Header** | wudfddi.h |
| **DLL** | WUDFx.dll |