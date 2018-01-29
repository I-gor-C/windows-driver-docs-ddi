---
UID : NN:wudfddi.IWDFDeviceInitialize2
title : IWDFDeviceInitialize2
author : windows-driver-content
description : The IWDFDeviceInitialize2 interface is a helper interface that allows a driver to specify a preferred buffer retrieval mode and buffer access method.
old-location : wdf\iwdfdeviceinitialize2.htm
old-project : wdf
ms.assetid : 78d0c888-955f-481f-aa59-f2e5eea1aa81
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : wdf.iwdfdeviceinitialize2, IWDFDeviceInitialize2 interface, IWDFDeviceInitialize2 interface, described, IWDFDeviceInitialize2, wudfddi/IWDFDeviceInitialize2, UMDFDeviceObjectRef_0a7dcdea-43e7-4a0a-b55c-34d18eca65e8.xml, umdf.iwdfdeviceinitialize2
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : wudfddi.h
req.include-header : Wudfddi.h
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 1.9
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

# IWDFDeviceInitialize2 interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IWDFDeviceInitialize2</b> interface is a helper interface that allows a driver to specify a preferred buffer retrieval mode and buffer access method.

## Methods

<p>The <b>IWDFDeviceInitialize2</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfddi.IWDFDeviceInitialize2.SetIoTypePreference](nf-wudfddi-iwdfdeviceinitialize2-setiotypepreference.md) | The SetIoTypePreference method specifies your preferences for how UMDF and the driver access the data buffers of a device's I/O requests. |

## Remarks

Drivers obtain the <b>IWDFDeviceInitialize2</b> interface by calling <b>IWDFDeviceInitialize::QueryInterface</b>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum UMDF version** | 1.9 |
| **Header** | wudfddi.h (include Wudfddi.h) |
| **DLL** | WUDFx.dll |