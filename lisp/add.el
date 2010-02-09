;;; add.el --- 

;; Copyright (C) 2003 Free Software Foundation, Inc.
;;
;; Author: Christoph Wedler <wedler@users.sourceforge.net>
;; Maintainer: (Please use `M-x x-symbol-package-bug' to contact the maintainer)
;; Version: 0.0
;; Keywords: WYSIWYG, LaTeX, HTML, wp, math, internationalization
;; X-URL: http://x-symbol.sourceforge.net/

;; This program is free software; you can redistribute it and/or modify
;; it under the terms of the GNU General Public License as published by
;; the Free Software Foundation; either version 2, or (at your option)
;; any later version.
;;
;; This program is distributed in the hope that it will be useful,
;; but WITHOUT ANY WARRANTY; without even the implied warranty of
;; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
;; GNU General Public License for more details.
;;
;; You should have received a copy of the GNU General Public License
;; along with this program; if not, write to the Free Software
;; Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

;;; Commentary:

;; If you want to use package x-symbol, please visit the URL (use
;; \\[x-symbol-package-web]) and read the info (use \\[x-symbol-package-info]).

;; 

;;; Code:

(provide 'add)

(defvar x-symbol-xsymb2-fonts
  '("-xsymb-xsymb2%s-medium-r-normal--%d-%d0-75-75-p-*-xsymb-xsymb2")
  "Fonts with registry/encoding \"xsymb-xsymb2\".
See `x-symbol-xsymb2-cset' and `x-symbol-init-cset'.")

(defvar x-symbol-xsymb2-cset
  '((("xsymb-xsymb2") ?\231 -3000)
    (xsymb2-left  "X-Symbol characters 1, left"  94 ?>) .
    (xsymb2-right "X-Symbol characters 1, right" 96 ?\?))
  "Cset with registry \"xsymb2\", see `x-symbol-init-cset'.")

(defvar x-symbol-xsymb2-table
  '(
    )
  "Table for registry \"xsymb2\", see `x-symbol-init-cset'.")

(x-symbol-init-cset x-symbol-xsymb2-cset x-symbol-xsymb2-fonts
		    x-symbol-xsymb2-table))

;;;  


;;; Local IspellPersDict: .ispell_xsymb
;;; add.el ends here
