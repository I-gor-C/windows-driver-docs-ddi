---
UID : NN:wudfddi.IWDFDriver
title : IWDFDriver
author : windows-driver-content
description : The IWDFDriver interface exposes the framework driver object that represents the driver image that is loaded in the host process.
old-location : wdf\iwdfdriver.htm
old-project : wdf
ms.assetid : ada475ae-e697-475c-b461-8e3a36ae9ab1
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : wdf.iwdfdriver, IWDFDriver interface, IWDFDriver interface, described, IWDFDriver, wudfddi/IWDFDriver, UMDFDriverObjectRef_2bce205e-d670-4dae-870a-f5b01c3ea49e.xml, umdf.iwdfdriver
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
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : Unavailable in UMDF 2.0 and later.
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : wudfddi.h
req.dll : WUDFx.dll
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PPOWER_ACTION, POWER_ACTION"
req.product : Windows 10 or later.
---

# IWDFDriver interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IWDFDriver</b> interface exposes the framework driver object that represents the driver image that is loaded in the host process.

## Methods

<p>The <b>IWDFDriver</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfddi.IWDFDriver.CreateDevice](nf-wudfddi-iwdfdriver-createdevice.md) | The CreateDevice method configures and creates a new framework device object. |
| [wudfddi.IWDFDriver.CreatePreallocatedWdfMemory](nf-wudfddi-iwdfdriver-createpreallocatedwdfmemory.md) | The CreatePreallocatedWdfMemory method creates a framework memory object for the specified buffer. |
| [wudfddi.IWDFDriver.CreateWdfMemory](nf-wudfddi-iwdfdriver-createwdfmemory.md) | The CreateWdfMemory method creates a framework memory object and allocates, for the memory object, a data buffer of the specified nonzero size. |
| [wudfddi.IWDFDriver.CreateWdfObject](nf-wudfddi-iwdfdriver-createwdfobject.md) | The CreateWdfObject method creates a custom (or user) WDF object from a parent WDF object. |
| [wudfddi.IWDFDriver.IsVersionAvailable](nf-wudfddi-iwdfdriver-isversionavailable.md) | The IsVersionAvailable method determines whether the specified version of the framework is available. |
| [wudfddi.IWDFDriver.RetrieveVersionString](nf-wudfddi-iwdfdriver-retrieveversionstring.md) | The RetrieveVersionString method retrieves the version of the framework. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum UMDF version** | 1.5 |
| **Header** | wudfddi.h |
| **DLL** | WUDFx.dll |