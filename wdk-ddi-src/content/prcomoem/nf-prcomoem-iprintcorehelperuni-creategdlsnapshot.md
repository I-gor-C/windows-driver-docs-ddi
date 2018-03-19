---
UID: NF:prcomoem.IPrintCoreHelperUni.CreateGDLSnapshot
title: IPrintCoreHelperUni::CreateGDLSnapshot method
author: windows-driver-content
description: The IPrintCoreHelperUni::CreateGDLSnapshot method creates a GDL snapshot of the driver configuration file based on the current configuration.
old-location: print\iprintcorehelperuni_creategdlsnapshot.htm
old-project: print
ms.assetid: 3dd9c7f9-27d4-45d2-8692-4270818c1823
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: CreateGDLSnapshot method [Print Devices], CreateGDLSnapshot method [Print Devices], IPrintCoreHelperUni interface, CreateGDLSnapshot,IPrintCoreHelperUni.CreateGDLSnapshot, IPrintCoreHelperUni, IPrintCoreHelperUni interface [Print Devices], CreateGDLSnapshot method, IPrintCoreHelperUni::CreateGDLSnapshot, prcomoem/IPrintCoreHelperUni::CreateGDLSnapshot, print.iprintcorehelperuni_creategdlsnapshot, print_unidrv-pscript_allplugins_c45d077d-295f-4636-829f-8595d43cd5ed.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: prcomoem.h
req.include-header: Prcomoem.h
req.target-type: Desktop
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
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	prcomoem.h
api_name:
-	IPrintCoreHelperUni.CreateGDLSnapshot
product: Windows
targetos: Windows
req.typenames: OEMPTOPTS, *POEMPTOPTS
req.product: Windows 10 or later.
---


# CreateGDLSnapshot method
The <code>IPrintCoreHelperUni::CreateGDLSnapshot</code> method creates a GDL snapshot of the driver configuration file based on the current configuration.

## Syntax

````
HRESULT CreateGDLSnapshot(
  [in]  PDEVMODE pDevmode,
  [in]  DWORD    cbSize,
  [in]  DWORD    dwFlags,
  [out] LPSTREAM *ppSnapshotStream
);
````

## Parameters

`pDevmode`

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure. If this pointer is provided, <code>IPrintCoreHelperUni::CreateGDLSnapshot</code>  should use the DEVMODEW structure that is pointed to by <i>pDevmode</i> instead of the default or current DEVMODEW structure. If this method is called from the plug-in provider, there is no default DEVMODEW structure and the <i>pDevmode</i> parameter is required.

`cbSize`

The size, in bytes, of the DEVMODEW structure that is pointed to by the <i>pDevmode</i> parameter.

`dwFlags`

Reserved for system use. This parameter must be set to zero.

`ppSnapshotStream`

A pointer to a stream that supplies the XML version of the GDL snapshot.


## Return Value

<code>IPrintCoreHelperUni::CreateGDLSnapshot</code> should return S_OK if the operation succeeds. Otherwise, this method should return a standard COM error code.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Desktop |
| **Header** | prcomoem.h (include Prcomoem.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff552917">IPrintCoreHelperUni::CreateDefaultGDLSnapshot</a>



<a href="..\prcomoem\nn-prcomoem-iprintcorehelperuni.md">IPrintCoreHelperUni</a>