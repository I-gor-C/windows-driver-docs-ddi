---
UID : NF:ntstrsafe.RtlStringCbPrintfExW
title : RtlStringCbPrintfExW function
author : windows-driver-content
description : The RtlStringCbPrintfExW and RtlStringCbPrintfExA functions create a byte-counted text string, with formatting that is based on supplied formatting information.
old-location : kernel\rtlstringcbprintfex.htm
old-project : kernel
ms.assetid : 514a5b40-c9ba-4ed1-871d-fd6ffde583a6
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : RtlStringCbPrintfExW
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ntstrsafe.h
req.include-header : Ntstrsafe.h
req.target-type : Desktop
req.target-min-winverclnt : Available starting with Windows XP with Service Pack 1 (SP1).
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : RtlStringCbPrintfExW,RtlStringCbPrintfExA,RtlStringCbPrintfExW
req.alt-loc : Ntstrsafe.lib,Ntstrsafe.dll
req.ddi-compliance : 
req.unicode-ansi : RtlStringCbPrintfExW (Unicode) and RtlStringCbPrintfExA (ANSI)
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Ntstrsafe.lib
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : "*PBATTERY_REPORTING_SCALE, BATTERY_REPORTING_SCALE"
---


# RtlStringCbPrintfExW function
The <b>RtlStringCbPrintfExW</b> and <b>RtlStringCbPrintfExA</b> functions create a byte-counted text string, with formatting that is based on supplied formatting information.

## Syntax

````
NTSTATUS RtlStringCbPrintfExW(
  _Out_opt_ LPTSTR  pszDest,
  _In_      size_t  cbDest,
  _Out_opt_ LPTSTR  *ppszDestEnd,
  _Out_opt_ size_t  *pcbRemaining,
  _In_      DWORD   dwFlags,
  _In_opt_  LPCTSTR pszFormat,
                    ...
);
````

## Parameters

`pszDest`

A pointer to a caller-supplied buffer that receives a formatted, null-terminated string. The function creates this string from both the formatting string that is supplied by <i>pszFormat</i> and the function's argument list. The <i>pszDest</i> pointer can be <b>NULL</b>, but only if STRSAFE_IGNORE_NULLS is set in <i>dwFlags</i>.

`cbDest`

The size of the destination buffer, in bytes. The buffer must be large enough to contain the formatted string plus the terminating null character. 

For Unicode strings, the maximum number of bytes is NTSTRSAFE_MAX_CCH * sizeof(WCHAR). 

For ANSI strings, the maximum number of bytes is NTSTRSAFE_MAX_CCH * sizeof(char). 

If <i>pszDest</i> is <b>NULL</b>, <i>cbDest</i> must be zero.

`ppszDestEnd`

If the caller supplies a non-<b>NULL</b> address pointer then, after the operation completes, the function loads that address with a pointer to the destination buffer's resulting null string terminator.

`pcbRemaining`

If the caller supplies a non-<b>NULL</b> address pointer, the function loads the address with the number of unused bytes that are in the buffer pointed to by <i>pszDest</i>, including bytes used for the terminating null character.

`dwFlags`

One or more flags and, optionally, a fill byte. The flags are defined as follows:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>

`pszFormat`

A pointer to a null-terminated text string that contains <b>printf</b>-styled <a href="http://msdn.microsoft.com/en-us/library/56e442dc.aspx">formatting directives</a>. The <i>pszFormat</i> pointer can be <b>NULL</b>, but only if STRSAFE_IGNORE_NULLS is set in <i>dwFlags</i>.

``




## Return Value

The function returns one of the NTSTATUS values that are listed in the following table. For information about how to test NTSTATUS values, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565436">Using NTSTATUS Values</a>.
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>This <i>success</i> status means source data was present, the output string was created without truncation, and the resultant destination buffer is null-terminated.
<dl>
<dt><b>STATUS_BUFFER_OVERFLOW</b></dt>
</dl>This <i>warning</i> status means the operation did not complete due to insufficient space in the destination buffer. If STRSAFE_NO_TRUNCATION is set in <i>dwFlags</i>, the destination buffer is not modified. If the flag is not set, the destination buffer contains a truncated version of the created string.
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>This <i>error</i> status means the function received an invalid input parameter. For more information, see the following paragraph.

The function returns the STATUS_INVALID_PARAMETER value when:

## Remarks

<b>RtlStringCbPrintfExW</b> and <b>RtlStringCbPrintfExA</b> should be used instead of the following functions: 

<b>sprintf</b>

<b>swprintf</b>

_<b>snprintf</b>

_<b>snwprintf</b>

All of these functions accept a format string and a list of arguments, interpret them, and create a formatted string. The size, in bytes, of the destination buffer is provided to <b>RtlStringCbPrintfExW</b> and <b>RtlStringCbPrintfExA</b> to ensure that they do not write past the end of the buffer.

<b>RtlStringCbPrintfExW</b> and <b>RtlStringCbPrintfExA</b> add to the functionality of <a href="..\ntstrsafe\nf-ntstrsafe-rtlstringcbprintfw.md">RtlStringCbPrintf</a> by returning a pointer to the end of the destination string, as well as the number of bytes left unused in that string. Flags can be passed to the function for additional control.

Use <b>RtlStringCbPrintfExW</b> to handle Unicode strings and <b>RtlStringCbPrintfExA</b> to handle ANSI strings. The form you use depends on your data, as shown in the following table.

WCHAR

L"string"

<b>RtlStringCbPrintfExW</b>

<b>char</b>

"string"

<b>RtlStringCbPrintfExA</b>

If <i>pszDest</i> and <i>pszFormat </i>point to overlapping strings or if any argument strings overlap, the behavior of the function is undefined.

Neither <i>pszFormat</i> nor <i>pszDest</i> can be <b>NULL</b> unless the STRSAFE_IGNORE_NULLS flag is set, in which case either or both can be <b>NULL</b>. If <i>pszDest</i> is <b>NULL</b>, <i>pszFormat</i> must either be <b>NULL</b> or point to an empty string.

For more information about the safe string functions, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff565508">Using Safe String Functions</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntstrsafe.h (include Ntstrsafe.h) |
| **Library** |  |
| **IRQL** | PASSIVE_LEVEL |
| **DDI compliance rules** |  |

## See Also

<dl>
<dt>
<a href="..\ntstrsafe\nf-ntstrsafe-rtlstringcbvprintfexw.md">RtlStringCbVPrintfEx</a>
</dt>
<dt>
<a href="..\ntstrsafe\nf-ntstrsafe-rtlstringcchprintfw.md">RtlStringCchPrintf</a>
</dt>
<dt>
<a href="..\ntstrsafe\nf-ntstrsafe-rtlstringcchprintfexw.md">RtlStringCchPrintfEx</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlStringCbPrintfExW function%20 RELEASE:%20(1/4/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>