---
UID: NN:wudfddi.IWDFWorkItem
title: IWDFWorkItem
author: windows-driver-content
description: This interface exposes a work item object.
old-location: wdf\iwdfworkitem.htm
old-project: wdf
ms.assetid: F9EDA26E-92E0-4936-87B7-E1E2A02A9D96
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IWDFWorkItem, IWDFWorkItem interface, IWDFWorkItem interface, described, umdf.iwdfworkitem, wdf.iwdfworkitem, wudfddi/IWDFWorkItem
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: wudfddi.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 1.11
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
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	WUDFx.dll
api_name:
-	IWDFWorkItem
product:
- Windows
targetos: Windows
req.typenames: POWER_ACTION, *PPOWER_ACTION
req.product: Windows 10 or later.
---

# IWDFWorkItem interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

This interface exposes a work item object.

## Methods

<p>The <b>IWDFWorkItem</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IWDFWorkItem::Enqueue](nf-wudfddi-iwdfworkitem-enqueue.md) | The Enqueue method adds this interface's framework work-item object to the system's work-item queue. |
| [IWDFWorkItem::Flush](nf-wudfddi-iwdfworkitem-flush.md) | The Flush method returns after this interface's work item has been serviced. |
| [IWDFWorkItem::GetParentObject](nf-wudfddi-iwdfworkitem-getparentobject.md) | The GetParentObject method returns the parent framework object of this interface's work item. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **End of support** | Unavailable in UMDF 2.0 and later.  |
| **Target Platform** | Desktop |
| **Minimum UMDF version** | 1.11 |
| **Header** | wudfddi.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff560200">IWDFObject</a>