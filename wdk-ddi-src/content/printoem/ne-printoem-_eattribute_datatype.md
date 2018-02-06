---
UID: NE:printoem._EATTRIBUTE_DATATYPE
title: "_EATTRIBUTE_DATATYPE"
author: windows-driver-content
description: The EATTRIBUTE_DATATYPE enumerates the possible data types for a global attribute, feature attribute or option attribute.
old-location: print\eattribute_datatype.htm
old-project: print
ms.assetid: 51d3e768-11b1-411d-89b1-4fec19306b97
ms.author: windowsdriverdev
ms.date: 1/18/2018
ms.keywords: kADT_INT, printoem/kADT_DWORD, printoem/kADT_BOOL, kADT_UNKNOWN, printoem/kADT_UNKNOWN, printoem/kADT_UNICODE, kADT_SIZE, kADT_UNICODE, printoem/kADT_INT, print.eattribute_datatype, _EATTRIBUTE_DATATYPE, printoem/kADT_SIZE, printoem/kADT_ASCII, kADT_CUSTOMSIZEPARAMS, printoem/kADT_CUSTOMSIZEPARAMS, printoem/kADT_RECT, EATTRIBUTE_DATATYPE, EATTRIBUTE_DATATYPE enumeration [Print Devices], kADT_BOOL, printoem/kADT_BINARY, kADT_DWORD, kADT_RECT, kADT_BINARY, kADT_ASCII, printoem/EATTRIBUTE_DATATYPE, printoem/kADT_LONG, print_unidrv-pscript_allplugins_6cda9036-f339-4700-808e-06c8867e5ba0.xml, kADT_LONG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: printoem.h
req.include-header: Printoem.h
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
-	printoem.h
apiname:
-	EATTRIBUTE_DATATYPE
product: Windows
targetos: Windows
req.typenames: EATTRIBUTE_DATATYPE
req.product: Windows 10 or later.
---

# _EATTRIBUTE_DATATYPE Enumeration
The EATTRIBUTE_DATATYPE enumerates the possible data types for a global attribute, feature attribute or option attribute.

## Syntax
````
typedef enum _EATTRIBUTE_DATATYPE { 
  kADT_UNKNOWN           = 0,
  kADT_BOOL              = 1,
  kADT_INT               = 2,
  kADT_LONG              = 3,
  kADT_DWORD             = 4,
  kADT_ASCII             = 5,
  kADT_UNICODE           = 6,
  kADT_BINARY            = 7,
  kADT_SIZE              = 8,
  kADT_RECT              = 9,
  kADT_CUSTOMSIZEPARAMS  = 10
} EATTRIBUTE_DATATYPE;
````

## Constants

<table>
            
                <tr>
                    <td>kADT_ASCII</td>
                    <td>The attribute is an ASCII string.</td>
                </tr>
            
                <tr>
                    <td>kADT_BINARY</td>
                    <td>The attribute consists of binary data.</td>
                </tr>
            
                <tr>
                    <td>kADT_BOOL</td>
                    <td>The attribute is of type BOOL.</td>
                </tr>
            
                <tr>
                    <td>kADT_CUSTOMSIZEPARAMS</td>
                    <td>The attribute is an array containing CUSTOMPARAM_MAX (a constant defined in printoem.h) elements. Each element is a <a href="..\printoem\ns-printoem-_customsizeparam.md">CUSTOMSIZEPARAM</a> structure.</td>
                </tr>
            
                <tr>
                    <td>kADT_DWORD</td>
                    <td>The attribute is of type DWORD.</td>
                </tr>
            
                <tr>
                    <td>kADT_INT</td>
                    <td>The attribute is of type INT.</td>
                </tr>
            
                <tr>
                    <td>kADT_LONG</td>
                    <td>The attribute is of type LONG.</td>
                </tr>
            
                <tr>
                    <td>kADT_RECT</td>
                    <td>The attribute is of type RECT.</td>
                </tr>
            
                <tr>
                    <td>kADT_SIZE</td>
                    <td>The attribute is of type SIZE.</td>
                </tr>
            
                <tr>
                    <td>kADT_UNICODE</td>
                    <td>The attribute is a Unicode string.</td>
                </tr>
            
                <tr>
                    <td>kADT_UNKNOWN</td>
                    <td>The attribute is of unknown type.</td>
                </tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | printoem.h (include Printoem.h) |

    ## See Also

        <a href="..\printoem\ns-printoem-_customsizeparam.md">CUSTOMSIZEPARAM</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20EATTRIBUTE_DATATYPE enumeration%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>