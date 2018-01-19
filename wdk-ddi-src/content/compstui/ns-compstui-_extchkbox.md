---
UID : NS:compstui._EXTCHKBOX
title : _EXTCHKBOX
author : windows-driver-content
description : The EXTCHKBOX structure is used by CPSUI applications (including printer interface DLLs) for specifying an extended check box, which can be added to a property sheet page option.
old-location : print\extchkbox.htm
old-project : print
ms.assetid : b3b82474-d4e5-467c-93dc-30edac189c66
ms.author : windowsdriverdev
ms.date : 1/8/2018
ms.keywords : _EXTCHKBOX, *PEXTCHKBOX, EXTCHKBOX
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : compstui.h
req.include-header : Compstui.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : EXTCHKBOX
req.alt-loc : compstui.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : "*PEXTCHKBOX, EXTCHKBOX"
---

# _EXTCHKBOX structure
The EXTCHKBOX structure is used by CPSUI applications (including printer interface DLLs) for specifying an extended check box, which can be added to a property sheet page option.

## Syntax
````
typedef struct _EXTCHKBOX {
  WORD      cbSize;
  WORD      Flags;
  LPTSTR    pTitle;
  LPTSTR    pSeparator;
  LPTSTR    pCheckedName;
  ULONG_PTR IconID;
  WORD      wReserved[4];
  ULONG_PTR dwReserved[2];
} EXTCHKBOX, *PEXTCHKBOX;
````

## Members

        
            `cbSize`

            Size, in bytes, of the EXTCHKBOX structure.
        
            `dwReserved`

            Reserved, must be initialized to zero.
        
            `Flags`

            Bit flags, which can be one of the following:
        
            `IconID`

            One of the following icon identifiers:

<ul>
<li>
An icon resource identifier. This can be application-defined, or it can be one of the CPSUI-supplied, IDI_CPSUI-prefixed icon resource identifiers.

</li>
<li>
An icon handle. If a handle is specified, ECBF_ICONID_AS_HICON must be set in the <b>Flags</b> member.

</li>
</ul>
If this value is zero, an icon is not displayed.
        
            `pCheckedName`

            String identifier, representing the text to be displayed when the check box is checked. This can be a 32-bit pointer to a NULL-terminated string, or it can be a 16-bit string resource identifier with HIWORD set to zero.
        
            `pSeparator`

            String identifier, representing a separator character to be displayed between the checked name string and the selected option string This can be a 32-bit pointer to a NULL-terminated string, or it can be a 16-bit string resource identifier with HIWORD set to zero.
        
            `pTitle`

            String identifier, representing the check box title. This can be a 32-bit pointer to a NULL-terminated string, or it can be a 16-bit string resource identifier with HIWORD set to zero.
        
            `wReserved`

            Reserved, must be initialized to zero.

    ## Remarks
        An extended check box is a CPSUI-defined type of check box that can be associated with an <a href="..\compstui\ns-compstui-_optitem.md">OPTITEM</a> structure. An OPTITEM structure can have one extended check box or one extended push button associated with it.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | compstui.h (include Compstui.h) |

    ## See Also

        <dl>
<dt>
<a href="..\compstui\ns-compstui-_extpush.md">EXTPUSH</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20EXTCHKBOX structure%20 RELEASE:%20(1/8/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>