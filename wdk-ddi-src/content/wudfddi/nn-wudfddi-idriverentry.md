---
UID: NN:wudfddi.IDriverEntry
title: IDriverEntry
author: windows-driver-content
description: The IDriverEntry interface exposes the user-mode driver's main entry and exit points.
old-location: wdf\idriverentry.htm
old-project: wdf
ms.assetid: eae6f032-2f31-43e1-9ac0-38ccc4840580
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IDriverEntry, IDriverEntry interface, IDriverEntry interface, described, UMDFDriverObjectRef_83709367-02f2-433f-a20b-b98eff736657.xml, umdf.idriverentry, wdf.idriverentry, wudfddi/IDriverEntry
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: WUDFx.dll
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	Wudfddi.h
api_name:
-	IDriverEntry
product: Windows
targetos: Windows
req.typenames: POWER_ACTION, *PPOWER_ACTION
req.product: Windows 10 or later.
---

# IDriverEntry interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IDriverEntry</b> interface exposes the user-mode driver's main entry and exit points.

## Methods

<p>The <b>IDriverEntry</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IDriverEntry::OnDeinitialize](nf-wudfddi-idriverentry-ondeinitialize.md) | The OnDeinitialize method performs any operations that are necessary before a system unloads a driver. |
| [IDriverEntry::OnDeviceAdd](nf-wudfddi-idriverentry-ondeviceadd.md) | The OnDeviceAdd method adds a new device to a system. |
| [IDriverEntry::OnInitialize](nf-wudfddi-idriverentry-oninitialize.md) | The OnInitialize method performs any operations that are necessary to initialize a driver. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | wudfddi.h |