---
UID: NE:ntddstor._STORAGE_DEVICE_FORM_FACTOR
title: "_STORAGE_DEVICE_FORM_FACTOR"
author: windows-driver-content
description: Indicates the form factor of a storage device.
old-location: storage\storage_device_form_factor.htm
old-project: storage
ms.assetid: EE59767B-2504-4E5F-A442-60EEBEE70B59
ms.author: windowsdriverdev
ms.date: 2/16/2018
ms.keywords: ntddstor/PSTORAGE_DEVICE_FORM_FACTOR, FormFactorMemoryCard, FormFactor1_8Less, FormFactorPCIeBoard, FormFactor3_5, FormFactor1_8, FormFactorM_2, PSTORAGE_DEVICE_FORM_FACTOR enumeration pointer [Storage Devices], FormFactorDimm, ntddstor/FormFactormSata, ntddstor/STORAGE_DEVICE_FORM_FACTOR, FormFactormSata, FormFactor2_5, ntddstor/FormFactorPCIeBoard, ntddstor/FormFactor2_5, STORAGE_DEVICE_FORM_FACTOR enumeration [Storage Devices], ntddstor/FormFactor3_5, PSTORAGE_DEVICE_FORM_FACTOR, ntddstor/FormFactor1_8, _STORAGE_DEVICE_FORM_FACTOR, storage.storage_device_form_factor, ntddstor/FormFactorUnknown, *PSTORAGE_DEVICE_FORM_FACTOR, FormFactorUnknown, ntddstor/FormFactorEmbedded, ntddstor/FormFactor1_8Less, ntddstor/FormFactorM_2, FormFactorEmbedded, STORAGE_DEVICE_FORM_FACTOR, ntddstor/FormFactorDimm, ntddstor/FormFactorMemoryCard
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddstor.h
req.include-header: Ntddstor.h
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
req.dll: 
req.irql: 
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	Ntddstor.h
apiname:
-	STORAGE_DEVICE_FORM_FACTOR
product: Windows
targetos: Windows
req.typenames: "*PSTORAGE_DEVICE_FORM_FACTOR, STORAGE_DEVICE_FORM_FACTOR"
---

# _STORAGE_DEVICE_FORM_FACTOR Enumeration
Indicates the form factor of a storage device.

## Syntax
````
typedef enum _STORAGE_DEVICE_FORM_FACTOR { 
  FormFactorUnknown     = 0, // 0x0
  FormFactor3_5,
  FormFactor2_5,
  FormFactor1_8,
  FormFactor1_8Less,
  FormFactorEmbedded,
  FormFactorMemoryCard,
  FormFactormSata,
  FormFactorM_2,
  FormFactorPCIeBoard,
  FormFactorDimm
} STORAGE_DEVICE_FORM_FACTOR, *PSTORAGE_DEVICE_FORM_FACTOR;
````

## Constants

<table>
            
                <tr>
                    <td>FormFactor1_8</td>
                    <td>1.8 inch nominal form factor.</td>
                </tr>
            
                <tr>
                    <td>FormFactor1_8Less</td>
                    <td>Less than 1.8 inch nominal form factor.</td>
                </tr>
            
                <tr>
                    <td>FormFactor2_5</td>
                    <td>2.5 inch nominal form factor.</td>
                </tr>
            
                <tr>
                    <td>FormFactor3_5</td>
                    <td>3.5 inch nominal form factor.</td>
                </tr>
            
                <tr>
                    <td>FormFactorDimm</td>
                    <td>Dual in-line memory module (DIMM) slot form factor.</td>
                </tr>
            
                <tr>
                    <td>FormFactorEmbedded</td>
                    <td>The storage device is embedded on a board.</td>
                </tr>
            
                <tr>
                    <td>FormFactorM_2</td>
                    <td>M.2 form factor.</td>
                </tr>
            
                <tr>
                    <td>FormFactorMemoryCard</td>
                    <td>A memory card, such as SmartMedia or CompactFlash.</td>
                </tr>
            
                <tr>
                    <td>FormFactormSata</td>
                    <td>Mini-SATA (mSATA) form factor.</td>
                </tr>
            
                <tr>
                    <td>FormFactorPCIeBoard</td>
                    <td>PCI Express (PCIe) card form factor.</td>
                </tr>
            
                <tr>
                    <td>FormFactorUnknown</td>
                    <td>Unknown form factor.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddstor.h (include Ntddstor.h) |