---
UID: NN:wudfddi.IWDFNamedPropertyStore
title: IWDFNamedPropertyStore
author: windows-driver-content
description: The IWDFNamedPropertyStore interface exposes a property-store object.
old-location: wdf\iwdfnamedpropertystore.htm
old-project: wdf
ms.assetid: f31a88c1-468f-4756-a5fa-b4aa0b8fe51d
ms.author: windowsdriverdev
ms.date: 1/11/2018
ms.keywords: wdf.iwdfnamedpropertystore, IWDFNamedPropertyStore interface, IWDFNamedPropertyStore interface, described, IWDFNamedPropertyStore, wudfddi/IWDFNamedPropertyStore, UMDFPropertyStoreObjectRef_139eb19f-8bb7-42ba-ab86-44f5f35e0faf.xml, umdf.iwdfnamedpropertystore
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	WUDFx.dll
apiname:
-	IWDFNamedPropertyStore
product: Windows
targetos: Windows
req.typenames: "*PPOWER_ACTION, POWER_ACTION"
req.product: Windows 10 or later.
---

# IWDFNamedPropertyStore interface

<p class="CCE_Message">[<b>Warning:</b> UMDF 2 is the latest version of UMDF and supersedes UMDF 1.  All new UMDF drivers should be written using UMDF 2.  No new features are being added to UMDF 1 and there is limited support for UMDF 1 on newer versions of Windows 10.  Universal Windows drivers must use UMDF 2.  For more info, see <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2">Getting Started with UMDF</a>.]

The <b>IWDFNamedPropertyStore</b> interface exposes a property-store object.

## Methods

<p>The <b>IWDFNamedPropertyStore</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [wudfddi.IWDFNamedPropertyStore.GetNameAt](nf-wudfddi-iwdfnamedpropertystore-getnameat.md) | The GetNameAt method retrieves the name of a property. |
| [wudfddi.IWDFNamedPropertyStore.GetNameCount](nf-wudfddi-iwdfnamedpropertystore-getnamecount.md) | The GetNameCount method retrieves the number of properties in a property store. |
| [wudfddi.IWDFNamedPropertyStore.GetNamedValue](nf-wudfddi-iwdfnamedpropertystore-getnamedvalue.md) | The GetNamedValue method retrieves the value of a property. |
| [wudfddi.IWDFNamedPropertyStore.SetNamedValue](nf-wudfddi-iwdfnamedpropertystore-setnamedvalue.md) | The SetNamedValue method sets the value of a property. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **End of support** | Unavailable in UMDF 2.0 and later.  |
| **Target Platform** | Desktop |
| **Minimum UMDF version** | 1.5 |
| **Header** | wudfddi.h |